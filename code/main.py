"""
Module: main.py
Author: Collins, Samuel, Benita, David
Description: Tests some of the methods in the classes and adds to the log file.
Date created: April 5th 2025
Last Updated: April 28th 2025
"""


from module_tmp import log
from config import CONFIG
from classes.student import CSVStudentData
from classes.grades import GradeStats
import numpy as np


def main():
    log("Starting the project...")
    student_data = CSVStudentData()
    student_data.violin_plot("GPA")
    student_data.scatter_plot("Age", "GPA")
    student_data.whisker_box_plot("GPA")
    student_data.line_plot("Age", "GPA")
    

    grade_data = GradeStats()
    stats = grade_data.calculate_stats()
    grade_data.plot_grade_histogram('GPA')
    log(f"Grade stats: {stats}")


    older_students = student_data.query_boolean(student_data.df['Age'] > 20)
    print(f"Number of students older than 20: {len(older_students)}")
    
    print("\nTop Performers:")
    print(grade_data.get_top_performers())
    print("\nStruggling Students:")
    print(grade_data.find_struggling_students())
    print(f"\n{grade_data.probability_joint("Maths", "Chemistry")}")
    

    # Vector Operations
    a = np.array([3, 4])
    b = np.array([1, 0])
    point1 = [2, 3]
    point2 = [5, 7]

    grade_data.display_vector(a)
    grade_data.export_vector(a, "vector_a")

    pos_vec = student_data.position_vector(point1, point2)
    print("Position Vector:", pos_vec)


    unit = student_data.unit_vector(a)
    print("Unit Vector:", unit)

    proj_vec = student_data.projection_vector(a, b)
    print("Projection Vector:", proj_vec)

    dot_prod = student_data.dot_product(a, b)
    print("Dot Product:", dot_prod)

    angle = student_data.angle_between_vectors(a, b)
    print("Angle Between Vectors:", angle)

    orthogonal = student_data.is_orthogonal(a, b)
    print("Are Vectors Orthogonal?", orthogonal)

    

if __name__ == "__main__":
    main()
