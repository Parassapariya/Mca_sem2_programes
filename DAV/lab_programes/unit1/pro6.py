'''
Write a program to prompt users to enter a value;then check
whether the entered value is positive or negative value and
display a proper message.
'''

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")