#check whether string entered is a palindrome or not

def reverse_string(s):
    return s[::-1]

def is_palindrome(string):
    return string == reverse_string(string)

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
#Enter a string: madam
#The string is a palindrome.
