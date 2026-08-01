"""
Name: Yuansheng Liang
Student ID:
Course: CSCI 2120 - Python Programming for Data Analytics
Project: Student Academic Performance Predictor
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


class StudentModel:

    def __init__(self, df):

        self.df = df

    def prepare_data(self):

        encoder = LabelEncoder()

        categorical_columns = [
            "school",
            "sex",
            "address",
            "famsize",
            "Pstatus",
            "Mjob",
            "Fjob",
            "reason",
            "guardian",
            "schoolsup",
            "famsup",
            "paid",
            "activities",
            "nursery",
            "higher",
            "internet",
            "romantic",
            "study_level",
            "pass"
        ]

        for column in categorical_columns:
            self.df[column] = encoder.fit_transform(
                self.df[column]
            )

        X = self.df.drop(
            columns=[
                "pass",
                "final_grade"
            ]
        )

        y = self.df["pass"]

        return train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

    def train_knn(self):

        X_train, X_test, y_train, y_test = self.prepare_data()

        model = KNeighborsClassifier(
            n_neighbors=5
        )

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        print("\n========== KNN ==========")

        print(
            "Accuracy:",
            accuracy_score(
                y_test,
                predictions
            )
        )

        print(
            "Precision:",
            precision_score(
                y_test,
                predictions
            )
        )

        print(
            "Recall:",
            recall_score(
                y_test,
                predictions
            )
        )

        print(
            "F1 Score:",
            f1_score(
                y_test,
                predictions
            )
        )

        print("\nClassification Report")

        print(
            classification_report(
                y_test,
                predictions
            )
        )

    def train_decision_tree(self):

        X_train, X_test, y_train, y_test = self.prepare_data()

        model = DecisionTreeClassifier(
            random_state=42
        )

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        print("\n========== Decision Tree ==========")

        print(
            "Accuracy:",
            accuracy_score(
                y_test,
                predictions
            )
        )

        print(
            "Precision:",
            precision_score(
                y_test,
                predictions
            )
        )

        print(
            "Recall:",
            recall_score(
                y_test,
                predictions
            )
        )

        print(
            "F1 Score:",
            f1_score(
                y_test,
                predictions
            )
        )

        print("\nClassification Report")

        print(
            classification_report(
                y_test,
                predictions
            )
        )