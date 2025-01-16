#write a programe to enter 10 numbers and display largest odd number from the entered number
num=[]
for i in range(10):
    num.append(int(input("enter a number: ")))
    
print("numbers are: ",num)
print("largest odd number is: ",max([i for i in num if i%2!=0]))
    