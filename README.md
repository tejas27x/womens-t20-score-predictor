# 🏏 Women's T20 First Innings Score Predictor

## Overview

This project predicts the final first innings score in Women's T20 cricket matches using Machine Learning. The model uses live match information such as current score, wickets remaining, run rate, and recent scoring momentum to estimate the final innings total.

The project was built using historical Women's T20 ball-by-ball data from Cricsheet and deployed as an interactive Streamlit web application.

---

## Problem Statement

During a live T20 match, analysts, commentators, and fans often try to estimate the final score based on the current match situation. This project aims to provide a data-driven prediction of the final first innings score using Machine Learning.

---

## Dataset

**Source:** Cricsheet Women's T20 Ball-by-Ball Dataset

Dataset includes:

* Match information
* Teams
* Venue and city
* Ball-by-ball events
* Runs scored
* Wickets
* Innings details

Data was filtered to include:

* Women's Matches
* T20 Format
* 20-over Matches

---

## Features Used

### Categorical Features

* Batting Team
* Bowling Team
* City

### Numerical Features

* Current Score
* Balls Left
* Wickets Left
* Current Run Rate (CRR)
* Runs Scored in Last 5 Overs

---

## Feature Engineering

The following cricket-specific features were created:

* Current Score
* Current Run Rate (CRR)
* Balls Remaining
* Wickets Remaining
* Recent Momentum (Last 5 Overs Runs)

These features help the model capture match context and scoring trends.

---

## Machine Learning Pipeline

1. Data Extraction from YAML files
2. Data Cleaning and Filtering
3. Feature Engineering
4. Train-Test Split
5. One-Hot Encoding
6. Feature Scaling
7. XGBoost Regression Model
8. Model Evaluation
9. Streamlit Deployment

---

## Model

**Algorithm:** XGBoost Regressor

Why XGBoost?

* Handles non-linear relationships effectively
* Works well on structured tabular data
* Strong predictive performance

---

## Performance Metrics

| Metric   | Score     |
| -------- | --------- |
| R² Score | 0.96      |
| MAE      | 2.72 Runs |

### Interpretation

* R² = 0.96 indicates the model explains approximately 96% of score variation.
* MAE = 2.72 means predictions are off by about 3 runs on average.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Pickle

---

## Application

Users can enter:

* Batting Team
* Bowling Team
* City
* Current Score
* Overs Completed
* Wickets Fallen
* Runs in Last 5 Overs

The application predicts the expected final first innings score.

---


## Screenshots

### Application Interface

![Home Page](Screenshot%202026-06-13%20132521.png)

### Model Performance

![Performance](screenshots/phase_accuracy.png)

---

## Learning Outcome

This project was built to explore Machine Learning beyond Data Analytics and understand the complete ML workflow, including:

* Data preprocessing
* Feature engineering
* Model training
* Model evaluation
* Model deployment

It helped me gain hands-on experience with building an end-to-end Machine Learning application.

---

## Run Locally

```bash
git clone https://github.com/yourusername/womens-t20-score-predictor.git

cd womens-t20-score-predictor

pip install -r requirements.txt

streamlit run app.py
```

---

## Author

**Tejas Nathe**

GitHub: https://github.com/tejas27x

LinkedIn: https://linkedin.com/in/tejas-nathe
