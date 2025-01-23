'''
. Write a program to create a list of names; then define a function
to display all the elements in the received list. Call the function to
execute its statements and display all names in the list.
'''
def display_names(names):
    for name in names:
        print(name)

names = ["A", "B", "C", "D", "E"]
display_names(names)