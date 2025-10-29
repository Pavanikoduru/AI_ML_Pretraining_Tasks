# Task 1 - Healthcare: Patient Readmission Risk Prediction

Problem Description:

Unexpected hospital revisits frequently mean bigger bills alongside dangers to a person’s well-being.

To help people stay well, medical professionals - doctors alongside those who organize care - require forecasts that arrive promptly so they can step in before issues arise.

Target Users: Doctors, healthcare analysts, hospital administrators

Pain Points: Unpredicted readmissions, high costs, delayed interventions

Proposed AI/ML Solution:

Gather information - patient histories, test outcomes, crucial health stats - from hospitals.

Keep information in either Amazon’s S3 or Azure’s data storage; tidy it up employing AWS Glue likewise Azure Data Factory.

Figure out who’s likely to be back in the hospital within a month using either a Random Forest or an XGBoost approach.

Get the finished model working - either as a simple web tool doctors can use, built with Streamlit, or via a more versatile API created with Flask.

Keep tabs on how well the system is working via AWS CloudWatch.


Cloud & Tech Stack:

|   Component             |   Technology Used        |
|-------------------------|--------------------------|
| Data Storage            | AWS S3                   |
| ETL / Preprocessing     | AWS Glue                 |
| Model Training          | AWS SageMaker            |
| Model Deployment        | Flask / Streamlit        |
| Monitoring              | AWS CloudWatch           |


Expected Outcome:

Spots patients likely to face serious trouble before problems arise.

Keeps people out of the hospital again while boosting how well they’re looked after.

Hospitals can better share supplies thanks to this. It means smarter spending, so care isn’t impacted by shortages.


Architecture Diagram:

[Patient Records / Lab Data]

↓

[AWS S3 Storage]

↓

[ETL Preprocessing (AWS Glue)]

↓

[Model Training (XGBoost on SageMaker)]

↓

[Flask API / Streamlit Dashboard]

↓

[Doctors Receive Alerts]

↓

[Monitoring via CloudWatch]
