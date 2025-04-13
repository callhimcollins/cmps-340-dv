import pandas as pd
import matplotlib.pyplot as plt
from config import CONFIG
import seaborn as sns

class StudentDataVisualizer:
    def __init__(self):
        self.config = CONFIG

    def query(self, df, column, value):
        return df[df[column] == value]

    def plot_histogram(self, df, column):
        df[column].hist()
        plt.title(f"Histogram of {column}")
        plt.savefig(f"{self.config['VISUAL_PATH']}{column}_hist.png")


class CSVStudentData(StudentDataVisualizer):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(self.config["STUDENTS_CSV"])

    def violin_plot(self, column):
        sns.violinplot(data=self.df, x=column)
        plt.title(f"Violin plot for {column}")
        plt.savefig(f"{self.config['VISUAL_PATH']}{column}_violin.png")

    def scatter_plot(self, x_col, y_col):
        sns.scatterplot(data=self.df, x=x_col, y=y_col)
        plt.title(f"Scatter plot of {x_col} vs {y_col}")
        plt.savefig(f"{self.config['VISUAL_PATH']}scatter_{x_col}_{y_col}.png")
