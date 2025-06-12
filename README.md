# Bone Fracture Detection using YOLOv8

## Project Overview

This project aims to develop an automated system for accurately detecting bone fractures in X-ray images using Computer Vision. The primary objective is to provide a rapid and accurate diagnostic aid, particularly beneficial in medical emergencies and resource-limited environments. By automating fracture detection, the system can help minimize delayed or missed diagnoses and assist in prioritizing urgent cases.

## [cite_start]Why This Project? 

* **Accurate and Rapid Diagnosis:** In emergency medical contexts, timely and precise diagnoses are crucial. [cite_start]This project addresses this need by providing an automated solution. 
* [cite_start]**Resource-Limited Settings:** The automation of X-ray interpretation can significantly assist healthcare professionals in areas where resources or specialized personnel may be scarce. 
* [cite_start]**Workload Reduction & Error Prevention:** Automating the initial detection process can reduce the workload on medical staff and help prevent human errors, thereby improving patient care. 

## [cite_start]Dataset and Preprocessing 

[cite_start]The dataset used for this project consists of X-ray images, sourced from Roboflow Universe. [cite_start]Each image is accompanied by a label file that specifies the location and type of fracture using bounding boxes.

### [cite_start]Fracture Classes Included: 
Initially, the dataset contained 11 classes, which were refined to 7 to improve model efficiency and robustness. [cite_start]The primary fracture types focused on are: 
* [cite_start]Alvusion Fracture 
* [cite_start]Comminuted Fracture 
* [cite_start]Compression-Crush Fracture 
* [cite_start]Fracture Dislocation 
* [cite_start]GreenStick Fracture 
* [cite_start]HairLine Fracture 
* [cite_start]Impact Fracture 

### [cite_start]Preprocessing Steps: 
* **Label Verification:** Ensured high-quality annotations by removing noisy data to prevent the model performance from dropping. [cite_start]This means keeping only high-quality, meaningful annotations. 
* [cite_start]**Class Cleaning:** Small classes and outliers with significantly less data were removed to prevent label noise and make the model more efficient in detecting the classes. 
* [cite_start]**Dataset Structure:** The processed dataset is organized into three sets: `train`, `valid`, and `test`. 
    * [cite_start]`train`: Used for model learning. 
    * [cite_start]`valid`: Used for tuning and monitoring during training. 
    * [cite_start]`test`: Used for final evaluation of the model's performance on unseen data. 

## [cite_start]Model and Training 

### [cite_start]Model Architecture 
[cite_start]The project utilizes **YOLOv8n (You Only Look Once v8 nano)**, an object detection architecture from Ultralytics. [cite_start]YOLO models are known for their speed and accuracy in real-time object detection. 

### [cite_start]Training Process 
[cite_start]The training process involves the following steps: 
1.  [cite_start]**Input Image:** An X-ray image is fed into the YOLOv8 model.
2.  [cite_start]**Forward Pass:** The neural network processes the image and generates predictions, including bounding boxes and class labels.
3.  **Loss Calculation:** These predictions are compared against the ground truth, and a loss function calculates the discrepancy. [cite_start]This `Loss` value is used to adjust model parameters.
4.  [cite_start]**Backpropagation:** The model uses the `Loss` value to adjust its parameters (weights) during training, which improves its performance.

### [cite_start]Training Configuration: 
[cite_start]The model was trained with the following parameters: 
* [cite_start]**Model:** `yolov8n.pt` (a pre-trained YOLOv8 nano model) 
* [cite_start]**Dataset Path:** `./Break-bone-3/data.yaml` 
* [cite_start]**Epochs:** 70 (An epoch represents a complete pass through the entire training dataset, allowing the model to learn and improve performance).
* [cite_start]**Image Size (`imgsz`):** 640 
* [cite_start]**Device:** `cpu` (for training on CPU) 
* [cite_start]**Batch Size:** 8 (A batch is a subset of the training data processed together in one forward and backward pass, leading to weight updates after a group of examples. A small batch means more updates, less memory, and possibly better generalization).

### [cite_start]Inference 
[cite_start]For inference (making predictions on new images), YOLO uses a single-pass process: 
1.  [cite_start]The image is divided into a grid. 
2.  [cite_start]The model directly predicts bounding boxes and class labels in one pass, making it very fast and efficient. 

## [cite_start]Results 

[cite_start]After 70 epochs of training, the model achieved promising results: 

* [cite_start]**Overall Mean Average Precision (mAP@0.5):** 0.721 (72.1%) 
* [cite_start]**Excellent Performance for Avulsion Fractures:** Achieved an mAP@0.5 of 0.854 (85.4%). 

| [cite_start]Class                   | mAP@0.5  [cite_start]| mAP@0.5:0.95  | [cite_start]Notes           |
| :---------------------- | :----------------- | :---------------------- | :------------------------ |
| Avulsion Fracture       | [cite_start]0.854               | [cite_start]0.333                    | [cite_start]Excellent detection        |
| Comminuted Fracture     | [cite_start]0.729               | [cite_start]0.277                    | [cite_start]Solid performance          |
| Compression-Crush Frac. | [cite_start]0.776               | [cite_start]0.398                    | [cite_start]Highest score              |
| GreenStick Fracture     | [cite_start]0.685               | [cite_start]0.244                    | [cite_start]Stable, decent             |
| HairLine Fracture       | [cite_start]0.734               | [cite_start]0.260                    | [cite_start]Good                       |
| Impact Fracture         | [cite_start]0.655               | [cite_start]0.267                    | [cite_start]Decent                     |
| Fracture Dislocation    | [cite_start]0.614               | [cite_start]0.211                    | [cite_start]Could improve              |

* **mAP@0.5:0.95:** It is important to note that the mAP@0.5:0.95 score is lower, as it requires more precise localization. [cite_start]This highlights some limitations of the model in more challenging cases, such as small fractures or overlapping areas. 

### [cite_start]Visual Results: 
[cite_start]The repository includes visual comparisons of labeled ground truth versus model predictions, demonstrating the model's ability to efficiently detect fractures in most cases. 

### [cite_start]Precision-Recall Curve: 
The precision-recall curve provides insights into the model's performance for each class. [cite_start]Classes with curves closer to the upper-right corner indicate strong performance (high precision and recall). 

### [cite_start]Normalized Confusion Matrix: 
[cite_start]The confusion matrix highlights which classes are most accurately predicted and where confusions occur: 
* [cite_start]**Most Accurately Predicted:** Avulsion (82%), Comminuted (81%), Compression-Crush (79%) 
* **Frequent Confusions:** Some fractures classified as background (up to 28%); [cite_start]HairLine and Fracture Dislocation also show some confusion.

## [cite_start]Demo 

A Streamlit-based application has been developed to demonstrate the automatic detection in action. [cite_start]Users can upload an X-ray image, and the application will process it through the trained model to display fracture predictions. 

## Conclusion

This project successfully demonstrates the application of Computer Vision for bone fracture detection, utilizing the YOLOv8 model. We achieved a promising mean Average Precision (mAP) of 0.721 for all classes after 70 epochs of training, with notable excellent performance for Avulsion Fractures (0.854 mAP). While there is always room for further improvement, particularly for certain fracture types and in achieving higher mAP@0.5:0.95 scores, the overall results underscore the significant potential of this automated diagnostic tool. This technology can contribute to more accurate and rapid diagnostics in critical medical situations, reducing workload and preventing potential errors. Further training and optimization efforts could lead to even higher accuracy and robustness.

## Setup and Usage

### Prerequisites
* Python 3.x
* PyTorch
* Ultralytics (for YOLOv8)
* OpenCV
* Streamlit (for the demo app)

### Installation
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
pip install -r requirements.txt