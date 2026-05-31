# cloud_RDS
# Cloud-Based Employee Management System using AWS RDS

## Project Title

Cloud-Based Employee Management System using Amazon RDS and Flask

## Intern ID:CITS783

---

## Project Overview

This project is a cloud-based employee management system developed using Python Flask and Amazon Relational Database Service (RDS). The system allows users to manage employee records through a web interface while storing data securely in a cloud-hosted MySQL database.

The project demonstrates how cloud databases can be integrated with web applications to provide scalable, reliable, and remotely accessible data storage.

---

## Objectives

* To understand cloud database services.
* To integrate Amazon RDS with a Flask application.
* To perform CRUD (Create, Read, Update, Delete) operations.
* To demonstrate cloud-based data management.
* To build a responsive employee management dashboard.

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend

* Python
* Flask
* SQLAlchemy

### Database

* Amazon RDS MySQL

### Cloud Platform

* Amazon Web Services (AWS)

---

## Project Features

### User Authentication

* Secure login page
* Session management

### Employee Management

* Add Employee
* View Employee List
* Update Employee Details
* Delete Employee Records

### Reports

* Total Employees Count
* Department-wise Employee Statistics
* Salary Summary

### Cloud Storage

* Employee data stored in AWS RDS MySQL
* Accessible from anywhere through the internet

---

## Project Structure

CloudRDSProject/

├── app.py

├── config.py

├── requirements.txt

├── README.md

├── templates/

│ ├── login.html

│ ├── dashboard.html

│ ├── add_employee.html

│ ├── employees.html

│ ├── edit_employee.html

│ └── reports.html

├── static/

│ └── css/

│ └── style.css

└── screenshots/

---

## AWS RDS Configuration

### Database Engine

MySQL Community Edition

### Region

Asia Pacific (Mumbai)

### DB Instance Identifier

database-1

### Database Name

cloudrds

### Port

3306

### Public Accessibility

Enabled

---

## Installation Steps

### Step 1: Clone or Download Project

Extract the project folder to your local machine.

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure AWS RDS

Update the database details in config.py:

```python
SECRET_KEY = "cloud_rds_secret_key"

DB_USER = "admin"

DB_PASSWORD = "YOUR_RDS_PASSWORD"

DB_HOST = "database-1.ctuk4si20nie.ap-south-1.rds.amazonaws.com"

DB_NAME = "cloudrds"
```

### Step 4: Run Application

```bash
python app.py
```

### Step 5: Open Browser

```text
http://127.0.0.1:5000
```

---

## Login Credentials

```text
Username: admin

Password: admin
```

---

## Database Schema

Employee Table

| Field      | Type         |
| ---------- | ------------ |
| id         | Integer      |
| name       | Varchar(100) |
| email      | Varchar(100) |
| department | Varchar(100) |
| salary     | Integer      |

---

## System Workflow

1. User opens application.
2. User logs in.
3. Dashboard is displayed.
4. User performs employee operations.
5. Flask processes requests.
6. SQLAlchemy communicates with AWS RDS.
7. Data is stored in MySQL cloud database.
8. Reports are generated from stored records.

---

## Advantages

* Cloud-based storage
* Centralized database management
* Secure data storage
* Easy scalability
* Remote accessibility
* Reduced maintenance overhead

---

## Future Enhancements

* User Registration Module
* Role-Based Access Control
* Employee Profile Images
* PDF Report Generation
* Email Notifications
* AWS CloudWatch Monitoring
* Backup and Recovery Automation

---

## Expected Output

* Login Page
* Dashboard Page
* Add Employee Page
* Employee List Page
* Reports Page

---

## Conclusion

The Cloud-Based Employee Management System successfully demonstrates the integration of Amazon RDS with a Flask web application. The project provides a practical implementation of cloud database concepts and showcases how organizations can securely manage employee information using cloud technologies.

---

## Developed For

Cloud Computing Internship Project

Project Title:
Cloud-Based Database Management System using AWS RDS
