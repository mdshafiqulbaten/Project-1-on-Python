# main.py

from student import Student
from gradebook import Gradebook

def main():
    gradebook = Gradebook()

    # Sample students
    gradebook.add_student(Student("S001", "Alice"))
    gradebook.add_student(Student("S002", "Bob"))

    while True:
        print("\nGradebook Menu:")
        print("1. Add Student")
        print("2. Record Grade")
        print("3. View Student Report")
        print("4. List All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            gradebook.add_student(Student(sid, name))
            print("Student added successfully.")

        elif choice == '2':
            sid = input("Enter Student ID: ")
            course = input("Enter Course Name: ")
            try:
                grade = float(input("Enter Grade (0-100): "))
                if 0 <= grade <= 100:
                    gradebook.record_grade(sid, course, grade)
                else:
                    print("Invalid grade. Must be 0-100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            sid = input("Enter Student ID: ")
            gradebook.student_report(sid)

        elif choice == '4':
            gradebook.display_all_students()

        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
