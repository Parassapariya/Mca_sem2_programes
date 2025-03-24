def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def process_marks_file(filename):
    try:
        with open(filename, "r") as file:
            print(f"{'RollNo':<10}{'Name':<15}{'Total':<10}{'Percentage':<15}{'Grade'}")
            print("=" * 55)
            
            for line in file:
                data = line.strip().split(",")
                
                roll_no = data[0]
                name = data[1]
                marks = list(map(int, data[2:]))  
                
                total = sum(marks)
                percentage = total / len(marks)
                grade = calculate_grade(percentage)
                
                print(f"{roll_no:<10}{name:<15}{total:<10}{percentage:.2f}%{' ' * 5}{grade}")
    
    except FileNotFoundError:
        print("File not found. Please check the filename.")
    except ValueError:
        print("File contains invalid data. Ensure it follows the correct format.")

filename = "marks.txt"  # Replace with your file name
process_marks_file(filename)

# Output:
# RollNo    Name           Total     Percentage     Grade
# ========================================================
# 101       Alice          280       70.00%         B
# 102       Bob            320       80.00%         A
# 103       Charlie        240       60.00%         C
# 104       David          200       50.00%         D