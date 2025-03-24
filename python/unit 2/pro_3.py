import logging

# Configure logging
logging.basicConfig(filename='example.log', level=logging.ERROR)

try:
    # Code that may raise an arithmetic exception
    result = 1 / 0  # Division by zero raises an exception
except ZeroDivisionError as e:
    # Log the exception
    logging.error(f"Exception occurred: {str(e)}")
    # Optionally handle the exception
    print("Cannot divide by zero!")
except Exception as e:
    # Handle any other exceptions
    logging.error(f"Exception occurred: {str(e)}")
    print(f"An error occurred: {str(e)}")
finally:
    # Optional cleanup or final statements
    print("Execution completed.")
