"""
Name: Yuansheng Liang
Student ID:
Course: CSCI 2120 - Python Programming for Data Analytics
Project: Student Academic Performance Predictor
"""

from data_processing import StudentDataProcessor
from visualization import StudentVisualizer
from model import StudentModel

def main():

    processor = StudentDataProcessor()

    processor.load_data()

    processor.data_summary()

    processor.clean_data()

    processor.feature_engineering()

    visualizer = StudentVisualizer(processor.df)

    visualizer.grade_distribution()
    
    visualizer.study_vs_grade()
    
    visualizer.average_grade_by_school()
    
    visualizer.grade_by_gender()
    
    visualizer.average_grade_by_study_level()

    model = StudentModel(processor.df)

    model.train_knn()

    model.train_decision_tree()


if __name__ == "__main__":
    main()