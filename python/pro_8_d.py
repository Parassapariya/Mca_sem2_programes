# Find and replace operation on string

def find_replace(string, find, replace):
    return string.replace(find, replace)

string = input("Enter a string: ")
find = input("Enter the word to find: ")
replace = input("Enter the word to replace: ")
print("Result:", find_replace(string, find, replace))
