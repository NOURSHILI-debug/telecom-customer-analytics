# telecom-customer-analytics
# Telecom DataFrame Exploration & Customer Analytics

This project provides an introductory exploration of a telecommunications customer dataset using Python.  
It focuses on loading, cleaning, analyzing, and manipulating tabular data using DataFrames, with the goal of understanding patterns in customer behavior and churn.

---

## Overview

The dataset (`telecom.csv`) contains information about approximately 6,000 customers of a fictional telecom company. It includes demographic data, subscribed services, billing details, and whether a customer has churned.

This project aims to demonstrate:

- Efficient DataFrame manipulation  
- Basic statistical exploration  
- Data filtering and selection  
- Sorting and summarizing customer information  
- Preparing the dataset for further analytics or machine learning tasks  

---

##  Dataset Description

Each row represents a customer, and each column describes an attribute such as:

- **customerID** – Unique client identifier  
- **gender** – Male / Female  
- **SeniorCitizen** – Indicates if the customer is a senior (1/0)  
- **Partner** – Whether the customer lives with a partner  
- **tenure** – Number of months as a customer  
- **PhoneService**, **MultipleLines**  
- **InternetService** – DSL, Fiber optic, or no service  
- **OnlineSecurity**, **StreamingTV**, **TechSupport**, etc.  
- **Contract** – Month-to-month, one-year, two-year  
- **PaperlessBilling**  
- **PaymentMethod**  
- **MonthlyCharges** – Current monthly bill  
- **TotalCharges** – Total amount paid  
- **Churn** – Whether the customer left the service  

These attributes are commonly used in churn prediction modeling and customer segmentation.

---
