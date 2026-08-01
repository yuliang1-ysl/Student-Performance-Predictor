# Student Academic Performance Predictor

## Project Description

This project is an individual project for CSCI 2120: Python Programming for Data Analytics.

The goal of this project is to analyze student academic performance using Python. The program loads and combines two student datasets, cleans the data, performs exploratory data analysis (EDA), creates visualizations, and trains machine learning models to predict whether a student will pass or fail.

---

## Dataset

This project uses the **Student Performance Dataset** from the UCI Machine Learning Repository.

Files used:

- student-mat.csv
- student-por.csv

The two datasets are combined into one dataset containing more than 500 records.

---

## Project Structure

```
Student_Performance_Project/
│
├── main.py
├── data_processing.py
├── visualization.py
├── model.py
├── student-mat.csv
├── student-por.csv
├── requirements.txt
└── README.md
```

---

## Features

- Load two CSV datasets
- Combine datasets into one DataFrame
- Clean and preprocess data
- Perform exploratory data analysis (EDA)
- Create data visualizations
- Train and evaluate classification models
- Predict student pass/fail status

---

## Python Libraries

The project uses the following libraries:

- pandas
- numpy
- matplotlib
- scikit-learn

---

## How to Run

1. Download or clone this repository.
2. Place the CSV files in the project folder.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the project:

```bash
python main.py
```

---

## Output

The program will:

- Load and combine the datasets
- Display a data summary
- Clean the data
- Generate charts
- Train machine learning models
- Display evaluation results

---

## Results

The project successfully:

- Combined two student datasets
- Performed data cleaning
- Created new features
- Generated five visualizations
- Trained two classification models
- Compared model performance

Decision Tree achieved higher accuracy than KNN.

---

## Author

Yuansheng Liang

CSCI 2120 – Python Programming for Data Analytics

Summer 2026