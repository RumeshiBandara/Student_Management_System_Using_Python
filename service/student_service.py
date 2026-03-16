from model.student import Student
from utils.file_handler import load_students, save_students


def add_student():
    students = load_students()
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")

    new_student = Student(student_id, name, age, course)
    students.append(new_student.to_dict())
    save_students(students)

    print("Student added successfully!")