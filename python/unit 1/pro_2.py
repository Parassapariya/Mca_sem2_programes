#write a program to input 2 numbers and one arithmatic oprator. perfom oprations as per arithmatic oprator which is given as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
oprator = input("Enter arithmatic oprator (+, -, *, /): ")

if oprator == "+":
    print(num1 + num2)
elif oprator == "-":
    print(num1 - num2)
elif oprator == "*":
    print(num1 * num2)
elif oprator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Error! Invalid arithmatic oprator.")


#Enter first number: 5
#Enter second number: 2
#Enter arithmatic oprator (+, -, *, /): +
#7