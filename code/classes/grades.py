"""
Module: Grades.py
Author: Benita, David
Description: Analyzes and visualizes student grades, including distributions, struggling students, and statistics.
Date: April 25th 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from config import CONFIG

class Grades:
    def __init__(self):
        self.df = pd.read_csv(CONFIG["GRADES_CSV"])
        self.student_id_col = 'StudentID' if 'StudentID' in self.df.columns else self.df.columns[0]
        self.numeric_cols = self.df.select_dtypes(include='float64').columns

    def get_grade_distribution(self, course):
        """Returns the distribution of letter grades for a course"""
        if course not in self.df.columns:
            raise ValueError(f"'{course}' not found in data")

        bins = [0, 60, 70, 80, 90, 100]
        labels = ['F', 'D', 'C', 'B', 'A']
        return pd.cut(self.df[course], bins=bins, labels=labels).value_counts().sort_index()


    def query_boolean(self, condition):
        return self.df[condition]

    def find_struggling_students(self, threshold=60, n=5):
        """Returns the bottom n struggling students with any course grade below the threshold"""
        mask = (self.df[self.numeric_cols] < threshold).any(axis=1)
        struggling = self.df[mask].copy()
        
        struggling['Average'] = struggling[self.numeric_cols].mean(axis=1)
        
        struggling = struggling.sort_values('Average').head(n)
        
        struggling.drop('Average', axis=1, inplace=True)
        
        return struggling[[self.student_id_col] + list(self.numeric_cols)]



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


class GradeStats(Grades):
    def calculate_stats(self):
        """Returns mean, median, and std for all courses"""
        return {
            "mean": self.df[self.numeric_cols].mean(),
            "median": self.df[self.numeric_cols].median(),
            "std": self.df[self.numeric_cols].std()
        }

    def get_top_performers(self, n=5):
        """Returns top n students by average grade"""
        self.df['Average'] = self.df[self.numeric_cols].mean(axis=1)
        top = self.df.sort_values('Average', ascending=False).head(n)
        self.df.drop('Average', axis=1, inplace=True)
        return top[[self.student_id_col] + list(self.numeric_cols)]


