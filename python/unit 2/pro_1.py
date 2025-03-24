try:
    # Code that may raise an exception
    x = 1 / 0  # Division by zero raises an exception
except ZeroDivisionError:
    # Handle the specific exception
    print("Cannot divide by zero!")
except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {str(e)}")
finally:
    # Optional cleanup or final statements
    print("Execution completed.")
