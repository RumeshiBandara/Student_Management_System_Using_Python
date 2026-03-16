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

def search_student():
    students = load_students()
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            return

    print("Student not found.")

def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print("Leave blank if you do not want to change a field.")

            new_name = input(f"Enter new name ({student['name']}): ")
            new_age = input(f"Enter new age ({student['age']}): ")
            new_course = input(f"Enter new course ({student['course']}): ")

            if new_name != "":
                student["name"] = new_name
            if new_age != "":
                student["age"] = new_age
            if new_course != "":
                student["course"] = new_course

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")