import os
import csv
import json

FILE_NAME = "students.txt"
CSV_FILE = "students.csv"
JSON_FILE = "students.json"


# ---------------- CREATE FILE ----------------
def create_file():
    with open(FILE_NAME, "a") as file:
        pass


# ---------------- ADD STUDENT ----------------
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    mark = input("Enter mark: ")

    data = f"{name},{age},{mark}\n"

    try:
        with open(FILE_NAME, "a") as file:
            file.write(data)

        print("Student added successfully!")

    except IOError:
        print("Error writing to file")


# ---------------- VIEW STUDENTS ----------------
def view_students():

    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()

            if content == "":
                print("No student records found")

            else:
                print("\nStudent Records")
                print("----------------")
                print(content)

    except FileNotFoundError:
        print("File not found")


# ---------------- UPDATE STUDENT ----------------
def update_student():

    old_name = input("Enter old student name: ")
    new_name = input("Enter new student name: ")

    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()

        updated_content = content.replace(old_name, new_name)

        with open(FILE_NAME, "w") as file:
            file.write(updated_content)

        print("Student updated successfully!")

    except IOError:
        print("Error updating file")


# ---------------- DELETE STUDENT ----------------
def delete_student():

    name = input("Enter student name to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:

            for line in lines:
                if not line.startswith(name + ","):
                    file.write(line)

        print("Student deleted successfully!")

    except IOError:
        print("Error deleting student")


# ---------------- EXPORT TO CSV ----------------
def export_csv():

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(CSV_FILE, "w", newline="") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(["Name", "Age", "Mark"])

            for line in lines:
                data = line.strip().split(",")
                writer.writerow(data)

        print("Data exported to CSV successfully!")

    except IOError:
        print("CSV export failed")


# ---------------- EXPORT TO JSON ----------------
def export_json():

    students = []

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

            for line in lines:
                name, age, mark = line.strip().split(",")

                student = {
                    "name": name,
                    "age": age,
                    "mark": mark
                }

                students.append(student)

        with open(JSON_FILE, "w") as jsonfile:
            json.dump(students, jsonfile, indent=4)

        print("Data exported to JSON successfully!")

    except IOError:
        print("JSON export failed")


# ---------------- RENAME FILE ----------------
def rename_file():

    if os.path.exists(FILE_NAME):

        os.rename(FILE_NAME, "student_backup.txt")

        print("File renamed successfully!")

    else:
        print("File not found")


# ---------------- MENU ----------------
def menu():

    create_file()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Export CSV")
        print("6. Export JSON")
        print("7. Rename File")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            export_csv()

        elif choice == "6":
            export_json()

        elif choice == "7":
            rename_file()

        elif choice == "8":
            print("Program exited")
            break

        else:
            print("Invalid choice")


# ---------------- START PROGRAM ----------------
menu()