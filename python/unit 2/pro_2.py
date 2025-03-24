# Define a custom exception class
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

try:
    # Raise the custom exception
    raise MyCustomException("This is a custom exception message.")
except MyCustomException as e:
    # Handle the custom exception
    print(f"Custom exception raised: {e.message}")


# Output:
# Custom exception raised: This is a custom exception message.
# Define a custom exception class
