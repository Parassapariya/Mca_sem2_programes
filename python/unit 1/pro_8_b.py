#Count Length of string (donot use len() )

def count_length(string):
    count = 0
    for i in string:
        count += 1
    return count

string = input("Enter a string: ")
print("Length of string is: ", count_length(string))