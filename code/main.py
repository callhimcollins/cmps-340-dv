from module_tmp import log
from config import CONFIG
from classes.student import CSVStudentData
from classes.grades import GradeStats

def main():
    log("Starting the project...")
    student_data = CSVStudentData()
    student_data.violin_plot("GPA")
    student_data.scatter_plot("Age", "GPA")
    

    grade_data = GradeStats()
    stats = grade_data.calculate_stats()
    log(f"Grade stats: {stats}")


if __name__ == "__main__":
    main()
