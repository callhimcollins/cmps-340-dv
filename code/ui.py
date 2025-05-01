"""
Module: UI.py
Author: Collins, Samuel
Description: Interact with the user and implements every method in parent and child classes.
Date created: April 26th 2025
Last Updated: April 28th 2025
"""

from module_tmp import log
from config import initial_prompt, view_stats, do_search, course_list
from classes.grades import GradeStats
from classes.student import CSVStudentData


student_obj = CSVStudentData()
grade_obj = GradeStats()

###first prompt to user
print("Welcome to CBDS High School.")
print(initial_prompt, end="")
prompt_response = input()

###loops till user exits
while(prompt_response != "0"):
    ###Option 1: perform a search
    if (prompt_response =="1"):
        print(do_search, end="")
        search_response = input()
        ##search sub-options
        while(search_response != "0"):
            ##find all the students in a department
            if search_response == "1":
                print("Enter department name:", end="")
                dep_name = input()
                print(student_obj.query(student_obj.df,"Major",dep_name))
                print(f"\n{do_search}", end="")
                search_response = input()
            #
            ##find the details of a particular student
            elif search_response == "2":
                print("Enter student name:")
                stu_name = input()
                print(student_obj.query(student_obj.df,"Name",stu_name))
                print(f"\n{do_search}", end="")
                search_response = input()
            #
            ##finds the 5 lowest GPAs
            elif search_response == "3":
                print("\nStruggling Students:")
                print(grade_obj.find_struggling_students())
                print(f"\n{do_search}", end="")
                search_response = input()
            #
            ##finds the top x students according to the user's input
            elif search_response == "4":
                print("Top? ", end="")
                top = int(input())
                print(f"\nTop {top} Performers:\n{grade_obj.get_top_performers(top)}\n{do_search}", end="")
                search_response = input()
            #
            ##Finds students above a certain GPA
            elif search_response == "5":
                print("Threshold: ", end="")
                try: 
                    thresh = float(input())
                    if thresh < 0:
                        message= "GPA cannot be negative!"
                        log(message)
                        raise ValueError(message)
                    #
                    condition = grade_obj.df["GPA"] > thresh
                    print(f"Students above {thresh} GPA:\n{grade_obj.query_boolean(condition)}\n{do_search}", end="")
                #
                except ValueError as e:
                     print(f"{e}\n{do_search}", end="")
                #
                search_response = input()
            #
            else:
                print(f"Invalid input. Retry!\n{do_search}", end="")
                search_response = input()
            #
        print(initial_prompt, end="")
        prompt_response = input()
    #

    ###Option 2: Visualizations.
    elif prompt_response == "2":
        print(view_stats, end="")
        stat_choice = input()
        ##visualization sub-options
        while stat_choice != "0":
            if stat_choice =="1": grade_obj.plot_grade_histogram("GPA")
            elif stat_choice == "2": student_obj.whisker_box_plot("GPA")
            elif stat_choice == "4": student_obj.violin_plot("GPA")
            elif stat_choice == "3": student_obj.scatter_plot("Age", "GPA")
            else:
                print("Wrong input! Retry: ", end="")
            #
            print(f"\n{view_stats}", end="")
            stat_choice = input()
        #
        print(initial_prompt, end="")
        prompt_response = input()
    #
    ###Option 3: Fun facts using probability
    elif prompt_response == "3":
        fact_count = 1
        print(f"{fact_count}. {grade_obj.age_vs_success()}")
        for i in range(len(course_list)):
            j = i + 1
            while(j < len(course_list)):
                fact_count += 1
                print(f"{fact_count}. {grade_obj.probability_joint(course_list[i],course_list[j])}")
                j += 1
            #
        #
        print(f"\n{initial_prompt}", end="")
        prompt_response = input()
    #
#
    
print("Thank you for using! Bye-bye!")   


