'''
1. Write a Python script to prompt users to enter two values;
then perform the basic arithmetical operations of addition,
subtraction, multiplication and division on the values.
'''

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "Undefined (division by zero)"

print("\nResults:")
print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")
