# Task 4 – Industrial Robotics: Assembly Line Quality Control

Problem Description:
Manufacturing lines produce thousands of products every hour, making manual inspection slow and error-prone.  
AI-powered computer vision can automatically detect defects, improving quality and reducing waste.

Target Users: Factory managers, quality control engineers, manufacturing companies  
Pain Points: Missed defects, human fatigue, inconsistent inspection quality

Proposed AI/ML Solution:
- Capture live camera feed from the production line.  
- Stream images or video frames to cloud storage (AWS S3 / Azure Blob).  
- Preprocess images (resize, normalize, enhance contrast).  
- Use a **CNN or YOLO (You Only Look Once)** model to detect defective products in real-time.  
- Train the model using **AWS SageMaker** or **Azure Machine Learning**.  
- Deploy inference models on **edge devices** near assembly lines for low-latency detection.  
- Generate automatic alerts and visualize defect metrics in a monitoring dashboard.


Cloud & Tech Stack:

|   Component           |   Technology Used                          |
|-----------------------|--------------------------------------------|
| Data Source           | Camera Feeds (IoT Cameras)                |
| Data Storage          | AWS S3 / Azure Blob Storage               |
| Model Training        | CNN / YOLO on AWS SageMaker / Azure ML    |
| Deployment            | Edge Inference using AWS IoT Greengrass / Azure IoT

