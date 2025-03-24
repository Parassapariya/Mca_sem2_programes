#armstrong number using 10 input and its armstrong find out and display it...

listofnumber = []

for i in range(2):
    num = int(input(f"Enter number {i+1}: "))
    listofnumber.append(num)

def is_armstrong(number):
    num_of_digits = len(str(number))
    sum_of_digits = sum(int(digit) ** num_of_digits for digit in str(number))
    return sum_of_digits == number

armstrong_numbers = []

for num in listofnumber:
    if is_armstrong(num):
        armstrong_numbers.append(num)

print("Armstrong numbers in the list:", armstrong_numbers)

#Enter number 1: 1
#Enter number 2: 50
#Armstrong numbers in the list: [1]
