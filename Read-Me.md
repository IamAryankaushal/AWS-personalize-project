# Personalized Recommendation System using Amazon Personalize

## Project Overview

This project demonstrates the development of a **real-time personalized recommendation system** using **Amazon Personalize**, an AWS-managed machine learning service. The system provides dynamic content recommendations based on user interactions, item metadata, and contextual data.

> This was a **group project** developed during an **AWS Cloud internship**, under the guidance of a mentor. Contributions were made collaboratively across design, implementation, and testing phases.

---

## Datasets Used

To simulate production-ready recommendation flows, three structured datasets were used during the initial phase:

- **Interactions Dataset** – Logs of user-item interactions (views, clicks, purchases)  
- **Items Dataset** – Metadata like item ID, category, price, and description  
- **Users Dataset** – (Optional) Contains attributes like age, location, and preferences  

These datasets were uploaded to **Amazon S3** and defined with JSON schemas compatible with **Amazon Personalize**.

---

## System Architecture

The system follows a **modular, serverless architecture** designed using **Python-based infrastructure-as-code**, suitable for rendering via tools like **AWS CDK** or **Graphviz**.

### Key Components

| Layer | Services |
|-------|----------|
| **Frontend** | Amazon API Gateway, Amazon CloudFront, Amazon Cognito |
| **Application** | AWS Lambda (recommendation logic), Amazon Personalize, DynamoDB |
| **Data Ingestion & Processing** | Kinesis Data Streams & Firehose, AWS Glue, EMR, EventBridge |
| **Storage** | Amazon S3 (raw, processed, lake), Amazon RDS |
| **Monitoring & Analytics** | CloudWatch, Athena |
| **Integration Layer** | Amazon SQS (for asynchronous communication) |

> The architecture is scalable, event-driven, and designed for real-time personalization with minimal latency.

---

## Project Workflow

1. **Upload Datasets** to Amazon S3  
2. **Create Dataset Group** in Amazon Personalize  
3. **Define Schemas** using Avro-compliant JSON  
4. **Import Datasets** into Personalize  
5. **Train Models** using AutoML (e.g., HRNN, SIMS)  
6. **Deploy Campaign** for real-time inference  
7. **Create Lambda Function** to call the Personalize runtime API  
8. **Expose via API Gateway** for external access  
9. **Query Recommendations** via REST endpoint

---

## Technologies Used

- **Amazon Personalize**  
- **AWS Lambda**  
- **Amazon S3**  
- **Amazon API Gateway**  
- **Amazon Cognito**  
- **Amazon Kinesis / AWS Glue / EMR**  
- **Amazon DynamoDB / RDS**  
- **CloudWatch & Athena**

---

## Key Features

- Real-time, low-latency recommendations  
- Serverless and scalable architecture  
- Uses AutoML for model selection and tuning  
- Cold-start solutions using popularity-based logic  
- Continuous model improvement with retraining loop  

---

## Security & Monitoring

- IAM-based access control  
- Cognito for secure user authentication  
- S3 encryption and lifecycle policies  
- CloudWatch logs, metrics, and dashboards  
- API rate limiting and input validation via API Gateway

---

## Optimization Notes

- Used S3 lifecycle rules for cost-effective data retention  
- Monitored costs via AWS Budgets and Cost Explorer  
- Auto-scaled compute and inference based on demand  
- Employed fallback recommendations for new users/items  

---

## Acknowledgment

This project was developed as a team effort during an **AWS Cloud internship**, with mentorship and collaborative contributions across all technical components and phases.

---

## License

This repository is intended for demonstration, educational, and professional portfolio purposes only.
