'''
Write a program to prompt users to enter a value; then check
whether the entered value is odd or even and display a proper
message.

'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")