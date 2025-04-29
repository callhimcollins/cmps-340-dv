"""
Module: Student.py
Author: David, Samuel
Description: Tools for visualizing student data with histograms, box plots, violin plots, and scatter plots, along with data querying and saving visualizations as image files.
Date: April 5th 2025
Last updated: April 28th 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
from config import CONFIG
import seaborn as sns
import numpy as np

class StudentDataVisualizer:
    def __init__(self):
        self.config = CONFIG
    
    def query(self, df, column, value):
        try:
            return df[df[column] == value]
        except:
            return f"{value} not found in {column}"
        
    def plot_histogram(self, df, column):
        """Generates a histogram for the given column in the DataFrame."""
        plt.figure(figsize=(6, 4))
        bins = np.arange(df[column].min(), df[column].max() + 2) - 0.5
        df[column].hist(bins=bins, edgecolor='black')
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Number of Students")
        plt.xticks(np.arange(df[column].min(), df[column].max() + 1))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(f"{self.config['VISUAL_PATH']}{column}_hist.png", dpi=300)
        plt.clf()
        print(f"figure saved in {self.config['VISUAL_PATH']}{column}_hist.png" )
    
    def whisker_box_plot(self, df, column):
        """Generates a box plot (whisker plot) for the given column."""
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=df, x=column, width=0.4, fliersize=5, linewidth=2)
        plt.title(f"Whisker Box Plot of {column}")
        plt.xlabel(column)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig(f"{self.config['VISUAL_PATH']}{column}_whiskerbox.png", dpi=300)
        plt.clf()
        print(f"figure saved in {self.config['VISUAL_PATH']}{column}_whiskerbox.png" )
    
    def violin_plot(self, df, column):
        """Generates a violin plot for the given column."""
        plt.figure(figsize=(6, 4))
        sns.violinplot(data=df, x=column)
        plt.title(f"Violin plot for {column}")
        plt.savefig(f"{self.config['VISUAL_PATH']}{column}_violin.png")
        plt.clf()
        print(f"figure saved in {self.config['VISUAL_PATH']}{column}_violin.png" )
    
    def scatter_plot(self, df, x_col, y_col):
        """Generates a scatter plot for the given x and y columns."""
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x=x_col, y=y_col)
        y_min, y_max = df[y_col].min(), df[y_col].max()
        y_ticks = np.linspace(y_min, y_max, num=6)
        plt.yticks(y_ticks)
        plt.xlim(19, 24)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Scatter plot of {x_col} vs {y_col}")
        plt.savefig(f"{self.config['VISUAL_PATH']}scatter_{x_col}_{y_col}.png")
        plt.clf()
        print(f"figure saved in {self.config['VISUAL_PATH']}scatter_{x_col}_{y_col}.png" )


class CSVStudentData(StudentDataVisualizer):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(self.config["STUDENTS_CSV"])
        self.plot_histogram(self.df, "Age")


    def query_boolean(self, condition):
        df = pd.read_csv(self.config["STUDENTS_CSV"])
        return df[condition]
    
    def whisker_box_plot(self, column):
        super().whisker_box_plot(self.df, column)
    
    def violin_plot(self, column):
        super().violin_plot(self.df, column)
    
    def scatter_plot(self, x_col, y_col):
        print(y_col)
        super().scatter_plot(self.df, x_col, y_col)
