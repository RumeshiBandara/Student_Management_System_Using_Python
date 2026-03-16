Student Management System (Python)

A simple console-based Student Management System developed using Python.
This application allows users to manage student records through a command-line interface with basic CRUD operations.

Features
Add new student records
View all students
Search student by ID
Update student information
Delete student records
Data persistence using JSON file storage

Project Structure
StudentManagementSystem
│
├── main.py
│
├── data
│   └── students.json
│
├── model
│   └── student.py
│
├── service
│   └── student_service.py
│
└── utils
    └── file_handler.py

Technologies Used
Python
JSON (for data storage)
IntelliJ / VS Code / PyCharm

System Architecture
The project follows a simple modular layered architecture:

main.py – Handles the main program flow and user menu
model – Defines the Student data structure
service – Contains business logic for managing students
utils – Handles file operations (JSON read/write)
data – Stores student records

Author
Rumeshi Bandara

