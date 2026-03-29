## Student Placement Prediction System

A Machine Learning web application that predicts whether a student is likely to be **placed or not placed** based on academic performance and skill-related attributes. The system uses a trained classification model and provides predictions through an interactive web interface.

---

## Live Demo

Web App:
https://placement-prediction-a0v7.onrender.com

---

## Project Overview

Campus placement depends on several factors such as academic performance, internships, projects, certifications, and communication skills.
This project uses machine learning to analyze these factors and predict placement outcomes.

The application allows users to input student details and receive a prediction about placement likelihood.

---

## Machine Learning Workflow

```
Data Collection
       ↓
Exploratory Data Analysis (EDA)
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Serialization (Pickle)
       ↓
Web Application
       ↓
Cloud Deployment
```


---

## Features Used for Prediction

* CGPA
* Branch
* College Tier
* Internships Count
* Projects Count
* Certifications Count
* Communication Skill Score
* Backlogs

---

## Technologies Used

Programming Language

* Python

Libraries

* Pandas
* NumPy
* Scikit-learn
* Pickle

Web Framework

* Streamlit

Deployment

* Render

---

## Project Structure

```
Placement-Prediction
│
├── artifacts
│   ├── model.pkl
│   └── Data_Preprocessing.pkl
│
├── notebook
│   ├── EDA.ipynb
│   └── cleanDF.csv
│
├── src
│   └── placement_prediction
│        └── components
│            └── Data Ingestion
|            └── Data Preprocessing
|            └── Model_trainer.py
│
├── app.py
├── requirements.txt
├── README.md
├── setup.py
├── template.py
```

---



## Model Performance

Accuracy: ~70%
Recall: ~80%

The model prioritizes recall to correctly identify students who are likely to be placed.

---

## Example Prediction

Input

```
CGPA: 8.5
Branch: Computer Science
College Tier: 1
Internships: 2
Projects: 3
Certifications: 4
Communication Score: 8
Backlogs: 0
```

Output

```
Student is likely to be PLACED
```

----



## Author

Omkar Kamate.

Aspiring Data Scientist / Machine Learning Engineer
