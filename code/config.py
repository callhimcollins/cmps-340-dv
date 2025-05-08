"""
Module: Grades.py
Author: Collins
Description: Holds long string that interacts with users to reduce redundance
Date created: April 5th 2025
Last Updated: April 28th 2025
"""


CONFIG = {
    "STUDENTS_CSV": "code/input/students.csv",
    "GRADES_CSV": "code/input/grades.csv",
    "VISUAL_PATH": "code/output/visualizations/",
    "PICKLE_PATH": "code/output/exports/gradeData",
}

initial_prompt = """What would you like to do?
1. Do a search.
2. View stats.
3. Fun facts.
0. Exit.
Response: 
"""
do_search = """Do you want to:
1. Search for students in a department.
2. Search for a student details.
3. Find struggling students.
4. Find best students.
5. Find students above a GPA threshold
0. Back
Response: """
view_stats = """Which of these do you want to view:
1. Histogram
2. Whisker box.
3. Scatter plot.
4. Violin plot.
0. Back.
Response: """

course_list = ["Math", "Biology", "Econ", "CS", "Physics", "Chemistry"]
