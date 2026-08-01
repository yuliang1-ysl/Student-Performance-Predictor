"""
Name: Yuansheng Liang
Student ID:
Course: CSCI 2120 - Python Programming for Data Analytics
Project: Student Academic Performance Predictor
"""

import matplotlib.pyplot as plt


class StudentVisualizer:

    def __init__(self, df):

        self.df = df

    def grade_distribution(self):

        plt.figure(figsize=(8, 6))

        plt.hist(
            self.df["final_grade"],
            bins=10
        )

        plt.title("Distribution of Final Grades")
        plt.xlabel("Final Grade")
        plt.ylabel("Number of Students")

        plt.show()

    def study_vs_grade(self):

        plt.figure(figsize=(8, 6))

        plt.scatter(
            self.df["studytime"],
            self.df["final_grade"]
        )

        plt.title("Study Time vs Final Grade")
        plt.xlabel("Study Time")
        plt.ylabel("Final Grade")

        plt.show()

    def average_grade_by_school(self):

        average = self.df.groupby(
            "school"
        )["final_grade"].mean()

        plt.figure(figsize=(6, 5))

        average.plot(
            kind="bar"
        )

        plt.title("Average Final Grade by School")
        plt.xlabel("School")
        plt.ylabel("Average Final Grade")

        plt.show()

    def grade_by_gender(self):

        plt.figure(figsize=(8, 6))

        self.df.boxplot(
            column="final_grade",
            by="sex"
        )

        plt.title("Final Grade by Gender")
        plt.suptitle("")

        plt.xlabel("Gender")
        plt.ylabel("Final Grade")

        plt.show()

    def average_grade_by_study_level(self):

        average = self.df.groupby(
            "study_level"
        )["final_grade"].mean()

        plt.figure(figsize=(6, 5))

        average.plot(
            kind="bar"
        )

        plt.title("Average Final Grade by Study Level")
        plt.xlabel("Study Level")
        plt.ylabel("Average Final Grade")

        plt.show()