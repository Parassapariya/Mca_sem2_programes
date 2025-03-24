class Student:
    def set_details(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll No: {self.roll_no}")

# Creating an object of the class
s1 = Student()

# Calling methods
s1.set_details("John Doe", 101)
s1.display_details()

# Output:
# Student Name: John Doe
# Roll No: 101
