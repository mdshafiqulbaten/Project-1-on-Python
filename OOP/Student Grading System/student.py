# student.py

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}  # course_name: grade

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        total_points = 0
        for grade in self.grades.values():
            total_points += self.convert_to_points(grade)
        return round(total_points / len(self.grades), 2)

    def convert_to_points(self, grade):
        if grade >= 90:
            return 4.0
        elif grade >= 80:
            return 3.0
        elif grade >= 70:
            return 2.0
        elif grade >= 60:
            return 1.0
        else:
            return 0.0

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, GPA: {self.calculate_gpa()}"
