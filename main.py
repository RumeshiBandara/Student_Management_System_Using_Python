from service.student_service import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")