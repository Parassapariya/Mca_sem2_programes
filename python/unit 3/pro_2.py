class Student:
    def __init__(self):
        self.roll_no = None
        self.name = None
        self.age = None
        self.gender = None

    def add_student(self):
        self.roll_no = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")
        print("Student details added successfully!\n")

    def display_student(self):
        print("\nStudent Details:")
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Creating an object of the class
s1 = Student()

# Adding and displaying student details
s1.add_student()
s1.display_student()

# Output:
# Enter Roll No: 101
# Enter Name: John Doe
# Enter Age
# Enter Gender: Male
# Student details added successfully!