#histograme print lines of * we can  input the numbers 

'''

print("Enter the numbers separated by space")
numbers = input()
numbers = [int(x) for x in numbers.split()]
for i in range(len(numbers)):
    print("*" * numbers[i])

'''

def histogram(values):
    for value in values:
        print('*' * value)

numbers = input()
numbers = [int(x) for x in numbers.split()]
histogram(numbers)


#Enter the numbers separated by space
#1 2 3 4 5 
#*
#**
#***
#****
#*****
