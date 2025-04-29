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

def main():
    log("Starting the project...")
    student_data = CSVStudentData()
    student_data.violin_plot("GPA")
    student_data.scatter_plot("Age", "GPA")
    student_data.whisker_box_plot("GPA")
    

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
    #print(f"\n{grade_data.age_vs_success()}")



    

if __name__ == "__main__":
    main()
