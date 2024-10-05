from flask import Flask, request, jsonify, render_template
import torch
import cv2
import numpy as np
import os

app = Flask(__name__)


model_path = 'D:\\Project\\Image processing\\cancer app\\cancer_detection\\models\\yolov5-master\\yolov5s.pt'
model = torch.hub.load('D:\\Project\\Image processing\\cancer app\\cancer_detection\\models\\yolov5-master', 'custom', path=model_path, source='local')


CANCER_CELL_CLASS_ID = 2  
MOTORCYCLE_CLASS_ID = 3   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file.'}), 400

 
    upload_folder = 'uploaded_images'
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    img = cv2.imread(file_path)
    results = model(img)

    detections = results.xyxy[0].numpy().tolist()

    
    cancer_cell_detected = any(detection[5] == CANCER_CELL_CLASS_ID for detection in detections)
    motorcycle_detected = any(detection[5] == MOTORCYCLE_CLASS_ID for detection in detections)

    return jsonify({
        'message': 'Image processed successfully!',
        'detections': detections,
        'cancer_cell_detected': cancer_cell_detected,
        'motorcycle_detected': motorcycle_detected
    })

@app.route('/live')
def live():
  
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return jsonify({'error': 'Could not open webcam.'}), 500
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        
        results = model(frame)
        result_img = results.render()[0]

     
        cv2.imshow('YOLOv5 Live Video Detection', result_img)

     
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    return jsonify({'message': 'Live detection ended.'})

if __name__ == '__main__':
    app.run(debug=True)
