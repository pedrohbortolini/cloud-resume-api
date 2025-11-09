# ⚡ Cloud Resume Challenge – Backend

🔗 Integrated with the website: [pedrobortolini.com.br](https://pedrobortolini.com.br)

This project is part of the **Cloud Resume Challenge**, where I developed the second stage of the challenge: creating a **serverless API** to record and display the number of website visitors.

---

## 🚀 Technologies Used

* **AWS Lambda (Python)** – function that processes requests and interacts with the database
* **Amazon DynamoDB** – NoSQL database that stores the visit counter
* **Amazon API Gateway** – exposes the Lambda function as a public HTTP API
* **JavaScript (frontend)** – consumes the API and updates the counter on the website

---

## 📌 Features

* Automatic increment of visits on each website access
* Persistent counter storage in DynamoDB
* **JSON** response consumed by the frontend
* **CORS** configuration restricted to the domain `pedrobortolini.com.br`

---

## 🔄 Workflow

1. The user accesses my website.
2. The **JavaScript** sends a `POST` request to the **API Gateway**.
3. The API Gateway triggers the **Lambda function**.
4. The Lambda updates the counter in **DynamoDB** and returns the updated value.
5. The **frontend** displays the real-time visitor count.
