"""
Module: UI.py
Author: Collins, Samuel
Description: Interact with the user and implements every method in parent and child classes.
Date created: April 26th 2025
Last Updated: April 28th 2025
"""

import numpy as np
import math as mth
from module_tmp import log
from config import initialPrompt, viewStats, doSearch, course_list
from classes.grades import GradeStats
from classes.student import CSVStudentData
studentObj = CSVStudentData()
gradeObj = GradeStats()


print("Welcome to CBDS High School.")
print(initialPrompt, end="")
promptResponse = input()
while(promptResponse != "0"):
    if (promptResponse =="1"):
        print(doSearch, end="")
        searchResponse = input()
        while(searchResponse != "0"):
            if searchResponse == "1":
                print("Enter department name:", end="")
                depName = input()
                print(studentObj.query(studentObj.df,"Major",depName))
                print(f"\n{doSearch}", end="")
                searchResponse = input()
            elif searchResponse == "2":
                print("Enter student name:")
                stuName = input()
                print(studentObj.query(studentObj.df,"Name",stuName))
                print(f"\n{doSearch}", end="")
                searchResponse = input()
            elif searchResponse == "3":
                print("\nStruggling Students:")
                print(gradeObj.find_struggling_students())
                print(f"\n{doSearch}", end="")
                searchResponse = input()
            elif searchResponse == "4":
                print("Top? ", end="")
                top = int(input())
                print(f"\nTop {top} Performers:\n{gradeObj.get_top_performers(top)}\n{doSearch}", end="")
                searchResponse = input()
            elif searchResponse == "5":
                print("Threshold: ", end="")
                try: 
                    thresh = float(input())
                    if thresh < 0:
                        message= "GPA cannot be negative!"
                        log(message)
                        raise ValueError(message)
                    condition = gradeObj.df["GPA"] > thresh
                    print(f"Students above {thresh} GPA:\n{gradeObj.query_boolean(condition)}\n{doSearch}", end="")
                except ValueError as e:
                     print(f"{e}\n{doSearch}", end="")
                searchResponse = input()
            else:
                print(f"Invalid input. Retry!\n{doSearch}", end="")
                searchResponse = input()
        print(initialPrompt, end="")
        promptResponse = input()
    elif promptResponse == "2":
        print(viewStats, end="")
        statChoice = input()
        while statChoice != "0":
            if statChoice =="1": gradeObj.plot_grade_histogram("GPA")
            elif statChoice == "2": studentObj.whisker_box_plot("GPA")
            elif statChoice == "4": studentObj.violin_plot("GPA")
            elif statChoice == "3": studentObj.scatter_plot("Age", "GPA")
            else:
                print("Wrong input! Retry: ", end="")
            print(f"\n{viewStats}", end="")
            statChoice = input()
        print(initialPrompt, end="")
        promptResponse = input()
    elif promptResponse == "3":
        fact_count = 1
        print(f"{fact_count}. {gradeObj.age_vs_success()}")
        for i in range(len(course_list)):
            j = i + 1
            while(j < len(course_list)):
                fact_count += 1
                print(f"{fact_count}. {gradeObj.probability_joint(course_list[i],course_list[j])}")
                j += 1
        print(f"\n{initialPrompt}", end="")
        promptResponse = input()





    
print("Bye!")   


