import numpy as np
import pandas as pd
from config import CONFIG


class Grades:
    def __init__(self):
        self.df = pd.read_csv(CONFIG["GRADES_CSV"])


class GradeStats(Grades):
    def __init__(self):
        self.df = pd.read_csv(CONFIG["GRADES_CSV"])

    def calculate_stats(self):
        numeric_df = self.df.select_dtypes(include='float64')
        return {
            "mean": numeric_df.mean(),
            "median": numeric_df.median(),
            "std": numeric_df.std()
        }
