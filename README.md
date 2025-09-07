# mlops-production-ready
This repo is to showcase the production ready deployment model

# 🛂 US Visa Approval Prediction

## 📌 Project Overview

This project focuses on predicting the **approval status of US visas** based on applicant features such as **degree**, **age**, **continent**, and more. By leveraging **machine learning classification algorithms**, we aim to develop a model that can predict whether a visa application will be **approved or rejected**.

---

## 🧩 Table of Contents

1. [Problem Statement](#-problem-statement)
2. [Solution Approach](#-solution-approach)
3. [Code Walkthrough](#-code-walkthrough)
4. [Deployment Overview](#-deployment-overview)

---

## ❗ Problem Statement

**US Visa Approval Status Classification**

Given a dataset containing features like:
- Education level
- Age
- Continent
- ...and more

The objective is to build a machine learning model to predict whether a US visa application will be **approved** or **rejected**.

> **Type**: Supervised Machine Learning  
> **Category**: Classification Problem

---

## 💡 Solution Approach

We follow a step-by-step ML pipeline to solve the problem:

1. **Data Loading**  
   Load visa application data from a database.

2. **Exploratory Data Analysis (EDA) & Feature Engineering**  
   - Understand data distribution and relationships.
   - Select relevant features and drop irrelevant/noisy ones.

3. **Model Training**  
   - Train multiple classification algorithms (e.g., Logistic Regression, Random Forest, etc.)
   - Compare model performances using standard metrics.

4. **Hyperparameter Tuning**  
   - Optimize top-performing models using techniques like GridSearchCV or RandomizedSearchCV.

5. **Model Selection**  
   - Choose the best model based on evaluation metrics such as accuracy, precision, recall, and F1-score.

---

## 🧭 Code Walkthrough

The code is structured in a modular way and follows standard ML best practices:

- `data_loader.py`: Connects to the database and loads the data.
- `eda.py`: Contains EDA and visual


## Commands

Create environment

```bash
conda create -n visa-prediction python=3.8 -y
```

```bash
conda activate visa-prediction
```

```bash
pip install -r requirements.txt
```

## Modules Usage

1. Logger Module
- used to save the print statement outputs to a file
- capture errors and logs into a file

