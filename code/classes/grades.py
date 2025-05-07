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
    bins = []
    labels = []
    def __init__(self):
        self.df = pd.read_csv(CONFIG["GRADES_CSV"])
        self.student_id_col = 'StudentID' if 'StudentID' in self.df.columns else self.df.columns[0]
        self.numeric_cols = self.df.select_dtypes(include='float64').columns
        export_pickle(self.df, "gradeData")

    def get_grade_distribution(self, course):
        """Returns the distribution of letter grades for a course"""
        if course not in self.df.columns:
            e =  ValueError(f"'{course}' not found in data")
            log(e)
            raise e
        self.bins = [0, 60, 70, 80, 90, 100]
        self.labels = ['F', 'D', 'C', 'B', 'A']
        
        return pd.cut(self.df[course], bins=self.bins, labels=self.labels).value_counts().sort_index()


    def query_boolean(self, condition):
        return self.df[condition]

    def find_struggling_students(self, threshold=60, n=5):
        struggling = self.df.sort_values('GPA', ascending=True).head(n)
        return struggling



    def plot_grade_histogram(self, course):
        """Saves a histogram plot of grades for a course"""
        plt.figure(figsize=(8, 5))
        plt.hist(self.df[course], bins=10, edgecolor='black')
        plt.title(f"{course} Grade Distribution")
        plt.xlabel("Grade")
        plt.ylabel("Number of Students")
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{CONFIG['VISUAL_PATH']}{course}_hist.png")
        plt.close()
        print(f"figure saved in {CONFIG['VISUAL_PATH']}{course}_hist.png" )


class GradeStats(Grades):
    def __init__(self):
        super().__init__()
        self.df = pd.read_pickle(f"{CONFIG['PICKLE_PATH']}")
        self.df2 = pd.read_csv(f"{CONFIG['STUDENTS_CSV']}")
    def calculate_stats(self):
        """Returns mean, median, and std for all courses"""
        return {
            "mean": self.df[self.numeric_cols].mean(),
            "median": self.df[self.numeric_cols].median(),
            "std": self.df[self.numeric_cols].std()
        }

    def get_top_performers(self, n=5):
        """Returns top n students by average grade"""
        topX = self.df.sort_values('GPA', ascending=False).head(n)
        return topX
    
    def probability_joint(self, course1,course2):
        noCourse1 = len(self.df2[(self.df2["Major"]== course1) & (self.df2["GPA"] >= 2.5)])
        noCourse2 = len(self.df2[(self.df2["Major"]== course2) & (self.df2["GPA"] >= 2.5)])
        totalStudents = len(self.df2)

        probability = lambda x: x / totalStudents
        prPassC1 = probability(noCourse1)
        prPassC2 = probability(noCourse2)

        if (prPassC1 > prPassC2):
            return f"Students studying {course1} are more likely to pass than those studying {course2}" 
        elif(prPassC1 == prPassC2):
            return f"Students studying {course2} are equally likely to pass than those studying {course1}"
        else: 
            return f"Students studying {course2} are more likely to pass than those studying {course1}"

    def age_vs_success(self):
        noOld = len(self.df2[self.df2["Age"]>20])
        noOfOldAndPass = len(self.df2[(self.df2["Age"]>20) & (self.df2["GPA"]>2.5)])
        prob = (noOfOldAndPass/noOld) * 100
        return f"The chances of a student with a GPA above 2.5, given that they are above 20 is {prob:.2f}%"

