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

def view_students():
    students = load_students()

    if len(students) == 0:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print("-" * 25)
