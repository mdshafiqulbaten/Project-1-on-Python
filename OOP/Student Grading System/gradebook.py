# gradebook.py

from student import Student

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def record_grade(self, student_id, course, grade):
        student = self.students.get(student_id)
        if not student:
            print("Student not found.")
            return
        student.add_grade(course, grade)
        print(f"Grade recorded for {student.name} in {course}.")

    def display_all_students(self):
        for student in self.students.values():
            print(student)

    def student_report(self, student_id):
        student = self.students.get(student_id)
        if not student:
            print("Student not found.")
            return
        print(f"\nReport for {student.name} (ID: {student.student_id})")
        for course, grade in student.grades.items():
            print(f"  {course}: {grade}")
        print(f"  GPA: {student.calculate_gpa()}\n")
