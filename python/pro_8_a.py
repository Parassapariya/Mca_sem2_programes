# Count Number of Vowel in given string
def count_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowel(string))