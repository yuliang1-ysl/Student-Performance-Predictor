"""
Name: Yuansheng Liang
Student ID:
Course: CSCI 2120 - Python Programming for Data Analytics
Project: Student Academic Performance Predictor
"""

import os
import pandas as pd


class StudentDataProcessor:

    def __init__(self):
        self.df = None

    def load_data(self):

        # Get the folder where this Python file is located
        folder = os.path.dirname(__file__)

        # Build full file paths
        math_path = os.path.join(folder, "student-mat.csv")
        por_path = os.path.join(folder, "student-por.csv")

        # Read CSV files
        math = pd.read_csv(math_path, sep=";")
        portuguese = pd.read_csv(por_path, sep=";")

        # Combine the two datasets
        self.df = pd.concat(
            [math, portuguese],
            ignore_index=True
        )

        return self.df

    def data_summary(self):

        print("========== DATA SUMMARY ==========")

        print("\nShape:")
        print(self.df.shape)

        print("\nColumns:")
        print(self.df.columns)

        print("\nData Types:")
        print(self.df.dtypes)

        print("\nFirst 5 Rows:")
        print(self.df.head())

        print("\nMissing Values:")
        print(self.df.isnull().sum())

        print("\nDuplicate Rows:")
        print(self.df.duplicated().sum())
    
    def clean_data(self):

        print("\n========== DATA CLEANING ==========")

        # Rename columns
        self.df.rename(columns={
            "G1": "first_grade",
            "G2": "second_grade",
            "G3": "final_grade"
        }, inplace=True)

        # Remove impossible grades
        self.df = self.df[
            (self.df["first_grade"] >= 0) &
            (self.df["first_grade"] <= 20) &
            (self.df["second_grade"] >= 0) &
            (self.df["second_grade"] <= 20) &
            (self.df["final_grade"] >= 0) &
            (self.df["final_grade"] <= 20)
        ]

        print("Cleaning completed.")
    
    def feature_engineering(self):

        # Pass or Fail
        self.df["pass"] = self.df["final_grade"].apply(
            lambda x: "Pass" if x >= 10 else "Fail"
        )

        # Study level
        self.df["study_level"] = self.df["studytime"].apply(
            lambda x: "High" if x >= 3 else "Low"
        )

        print("Feature engineering completed.")

        print()

        print(self.df[
            ["final_grade", "pass", "studytime", "study_level"]
        ].head())