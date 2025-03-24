#Write a program to create a function which accepts 2 numbers and one arithmetic operator. Return the answer accordingly.

def arithmetic_operations(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Error! Invalid arithmetic operator."
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter arithmetic operator (+, -, *, /): ")
print(arithmetic_operations(num1, num2, operator))

#Enter first number: 5
#Enter second number: 2
#Enter arithmetic operator (+, -, *, /): +
#7
