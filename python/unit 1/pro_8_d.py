# Find and replace operation on string

def find_replace(string, find, replace):
    return string.replace(find, replace)

string = input("Enter a string: ")
find = input("Enter the word to find: ")
replace = input("Enter the word to replace: ")
print("Result:", find_replace(string, find, replace))

#Enter a string: hello world
#Enter the word to find: world
#Enter the word to replace: universe
#Result: hello universe

