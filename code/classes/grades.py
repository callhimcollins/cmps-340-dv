"""
Module: Grades.py
Author: Benita, David
Description: Analyzes and visualizes student grades, including distributions, struggling students, and statistics.
Date created: April 5th 2025
Last Updated: April 27th 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from module_tmp import export_pickle, log
from config import CONFIG

class Grades:
    _bins = []
    _labels = []

    def __init__(self):
        self._df = pd.read_csv(CONFIG["GRADES_CSV"])
        self._student_id_col = 'StudentID' if 'StudentID' in self._df.columns else self._df.columns[0]
        self._numeric_cols = self._df.select_dtypes(include='float64').columns
        export_pickle(self._df, "gradeData")

    def get_grade_distribution(self, course):
        if course not in self._df.columns:
            e = ValueError(f"'{course}' not found in data")
            log(e)
            raise e
        self._bins = [0, 60, 70, 80, 90, 100]
        self._labels = ['F', 'D', 'C', 'B', 'A']
        return pd.cut(self._df[course], bins=self._bins, labels=self._labels).value_counts().sort_index()

    def query_boolean(self, condition):
        return self._df[condition]

    def find_struggling_students(self, threshold=60, n=5):
        struggling = self._df.sort_values('GPA', ascending=True).head(n)
        return struggling

    def plot_grade_histogram(self, course):
        plt.figure(figsize=(8, 5))
        plt.hist(self._df[course], bins=10, edgecolor='black')
        plt.title(f"{course} Grade Distribution")
        plt.xlabel("Grade")
        plt.ylabel("Number of Students")
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{CONFIG['VISUAL_PATH']}{course}_hist.png")
        plt.close()
        print(f"figure saved in {CONFIG['VISUAL_PATH']}{course}_hist.png")



class GradeStats(Grades):
    def __init__(self):
        super().__init__()
        self._df = pd.read_pickle(f"{CONFIG['PICKLE_PATH']}")
        self._df2 = pd.read_csv(f"{CONFIG['STUDENTS_CSV']}")

    def calculate_stats(self):
        return {
            "mean": self._df[self._numeric_cols].mean(),
            "median": self._df[self._numeric_cols].median(),
            "std": self._df[self._numeric_cols].std()
        }

    def get_top_performers(self, n=5):
        return self._df.sort_values('GPA', ascending=False).head(n)

    def probability_joint(self, course1, course2):
        noCourse1 = len(self._df2[(self._df2["Major"] == course1) & (self._df2["GPA"] >= 2.5)])
        noCourse2 = len(self._df2[(self._df2["Major"] == course2) & (self._df2["GPA"] >= 2.5)])
        totalStudents = len(self._df2)

        pr1, pr2 = noCourse1 / totalStudents, noCourse2 / totalStudents
        if pr1 > pr2:
            return f"Students studying {course1} are more likely to pass than those studying {course2}"
        elif pr1 == pr2:
            return f"Students studying {course2} are equally likely to pass as those studying {course1}"
        else:
            return f"Students studying {course2} are more likely to pass than those studying {course1}"

    def age_vs_success(self):
        older = self._df2[self._df2["Age"] > 20]
        passed = older[older["GPA"] > 2.5]
        prob = (len(passed) / len(older)) * 100 if len(older) else 0
        return f"The chances of a student with a GPA above 2.5, given that they are above 20 is {prob:.2f}%"


    def display_vector(self, vector):
        print("Vector:", vector)

    def export_vector(self, vector, filename, **kwargs):
        delimiter = kwargs.get("delimiter", ",")
        np.savetxt(f"{CONFIG['VISUAL_PATH']}{filename}.txt", vector, delimiter=delimiter)
        print(f"Vector saved to {CONFIG['VISUAL_PATH']}{filename}.txt")

    def position_vector(self, point1, point2):
        return np.array(point2) - np.array(point1)

    def unit_vector(self, vector):
        norm = np.linalg.norm(vector)
        return vector / norm if norm != 0 else np.zeros_like(vector)

    def projection_vector(self, a, b):
        b_unit = self.unit_vector(b)
        projection_length = np.dot(a, b_unit)
        return projection_length * b_unit

    def dot_product(self, a, b):
        return np.dot(a, b)

    def angle_between_vectors(self, a, b):
        dot_prod = self.dot_product(a, b)
        norms = np.linalg.norm(a) * np.linalg.norm(b)
        if norms == 0:
            return 0
        cos_theta = np.clip(dot_prod / norms, -1.0, 1.0)
        return np.degrees(np.arccos(cos_theta))

    def is_orthogonal(self, a, b, tol=1e-10):
        return abs(self.dot_product(a, b)) < tol
