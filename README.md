Why Focus on Lung Cancer?
- Lung cancer is highly dangerous, it often spreads to other organs (brain, bones). 
- Once occurred, it becomes nearly incurable. 
- Current diagnostic methods are slow, delaying treatment. 
- Our system Enable faster, more accurate detection and provide surgical assistance for better patient outcomes.

  ![image](https://github.com/user-attachments/assets/f52e2a8a-9e86-43ac-8ca2-556d1bf5ac4f)


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

![image](https://github.com/user-attachments/assets/37db970b-ab93-4e17-ad8a-fa884e6b980f)



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


![image](https://github.com/user-attachments/assets/63afde99-fae0-4d92-96d7-60aa79932dd7)

OUTPUT:
![val_batch0_labels](https://github.com/user-attachments/assets/1151f96a-b14f-41eb-a8be-a93ea2551118)












![val_batch0_pred](https://github.com/user-attachments/assets/255e90a9-0f6c-4fa6-bad0-2680f648b54f)












![val_batch0_pred](https://github.com/user-attachments/assets/9a23d30d-4709-4f1f-becf-62cd0cb915e2)

















![colonca744 - Copy](https://github.com/user-attachments/assets/91376690-4610-429a-970a-b2c8a31f6f2e)













