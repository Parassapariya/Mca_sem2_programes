import os

FILENAME = "students.txt"

def add_student():
    with open(FILENAME, "a") as file:
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks (comma-separated): ")
        file.write(f"{roll_no},{name},{marks}\n")
        print("Student added successfully!\n")

def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll_no:
                print("Student Found: ", " | ".join(data))
                found = True
                break
    if not found:
        print("Student not found!\n")

def list_students():
    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        print("No students found.\n")
        return
    with open(FILENAME, "r") as file:
        print("\nRoll No  | Name      | Marks")
        print("=" * 30)
        for line in file:
            data = line.strip().split(",")
            print(f"{data[0]:<8} | {data[1]:<10} | {data[2]}")
        print()

def update_student():
    roll_no = input("Enter Roll No to update: ")
    found = False
    students = []
    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll_no:
                name = input("Enter new name: ")
                marks = input("Enter new marks (comma-separated): ")
                students.append(f"{roll_no},{name},{marks}\n")
                found = True
            else:
                students.append(line)
    
    if found:
        with open(FILENAME, "w") as file:
            file.writelines(students)
        print("Student updated successfully!\n")
    else:
        print("Student not found!\n")

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    found = False
    students = []
    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll_no:
                found = True
                continue
            students.append(line)
    
    if found:
        with open(FILENAME, "w") as file:
            file.writelines(students)
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")

while True:
    print("Student Management System")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")
    
    choice = input("Enter your choice: ").lower()
    
    if choice == 'a':
        add_student()
    elif choice == 'b':
        search_student()
    elif choice == 'c':
        list_students()
    elif choice == 'd':
        update_student()
    elif choice == 'e':
        delete_student()
    elif choice == 'f':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please try again.\n")

# Output:
# Student Management System
# a) Add Student
# b) Search Student
# c) List All Students
# d) Update Student
# e) Delete Student
# f) Exit
# Enter your choice: a
# Enter Roll No: 101
# Enter Name: Alice
# Enter Marks (comma-separated): 90,80,70
# Student added successfully!