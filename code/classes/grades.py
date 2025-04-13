import numpy as np
import pandas as pd
import pickle
from config import CONFIG


class VectorAnalysis:
    def dot_product(self, v1, v2):
        return np.dot(v1, v2)

    def angle_between(self, v1, v2):
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.arccos(cos_angle)

    def is_orthogonal(self, v1, v2):
        return np.isclose(self.dot_product(v1, v2), 0)


class GradeStats(VectorAnalysis):
    def __init__(self):
        self.df = pd.read_csv(CONFIG["GRADES_CSV"])

    def calculate_stats(self):
        numeric_df = self.df.select_dtypes(include='number')
        return {
            "mean": numeric_df.mean(),
            "median": numeric_df.median(),
            "std": numeric_df.std()
        }


    def joint_probabilities(self, col1, col2):
        joint_counts = pd.crosstab(self.df[col1], self.df[col2])
        return joint_counts / joint_counts.sum().sum()
