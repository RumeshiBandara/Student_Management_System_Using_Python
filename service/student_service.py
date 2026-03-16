from model.student import Student
from utils.file_handler import load_students, save_students


def add_student():
    students = load_students()
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return