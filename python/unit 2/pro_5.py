def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Contents:\n")
            print(content)
            words = content.split()
            print("\nTotal number of words:", len(words))
    except FileNotFoundError:
        print("File not found. Please check the filename.")

filename = "sample.txt"  # Replace with your file name
read_file(filename)

# File Contents:
# This is a sample text file.