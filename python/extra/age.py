try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 150:
        raise ValueError("Enter a valid age")
except ValueError as e:
    print(e)
else:
    if age > 18:
        print("You are eligible for vote.")
    else:
        print("You are not eligible for vote.")
finally:
    print("Program execution completed.")
