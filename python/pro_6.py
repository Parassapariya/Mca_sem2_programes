#histograme print lines of * we can  input the numbers 

print("Enter the numbers separated by space")

numbers = input()

numbers = [int(x) for x in numbers.split()]

for i in range(len(numbers)):
    print("*" * numbers[i])
