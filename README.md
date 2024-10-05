![image](https://github.com/user-attachments/assets/7a6b3b2a-27b0-4969-8a72-edf1911e6458)Why Focus on Lung Cancer?
- Lung cancer is highly dangerous, it often spreads to other organs (brain, bones). 
- Once occurred, it becomes nearly incurable. 
- Current diagnostic methods are slow, delaying treatment. 
- Our system Enable faster, more accurate detection and provide surgical assistance for better patient outcomes.

CHALLENGES IN LUNG CANCER DIAGNOSIS AND SURGERY
Slow Diagnosis: Current biopsy analysis takes 7–10 days.
Manual Interpretation: Reliant on pathologists; prone to human error.
Surgical Precision: Difficult to ensure complete removal of cancerous tissue during surgery.
Metastasis Risk: Late-stage detection worsens survival rates.
Goal: An automated system to improve accuracy and speed in both diagnosis and surgery.

Technology Stack
YOLOv5s: Used for detecting cancer cells in biopsy images.
Intel oneAPI: Optimizes performance for image processing and real-time analysis.
Flask: Web framework for interfacing with doctors.
OpenCV: Handles image preprocessing.
HTML/CSS/JavaScript: For front-end interface.
PyTorch: Runs the YOLOv5s mode

SELECTION OF YOLO V5:
Efficient for real time object detection.
Minute pixels classification
Friendly user interface over recent ml algorithms 


Encoder:
Processes input sequence 
X=(x1,x2,...,xM)
X = (x_1, x_2, ..., x_M)
-X=(x1 ,x2 ,...,xM ), where xix_ixi  represents each word.
Outputs a hidden state for each word:
hi=EncoderRNN(xi,hi−1)
h_i = \text{EncoderRNN}(x_i, h_{i-1})
Decoder:
The probability of the target sentence
 Y=(y1,y2,...,yN)
Y = (y_1, y_2, ..., y_N)
Y=(y1 ,y2 ,...,yN ) given the source sentence XXX is: P(Y∣X)=∏n=1NP(yn∣y1,...,yn−1,X)
Predicts the next word yny_nyn  based on all previous words 
      and the source sentence.










