#write a programe to enter 10 numbers and display largest odd number from the entered number
num=[]
for i in range(10):
    num.append(int(input("enter a number: ")))
    
print("numbers are: ",num)
print("largest odd number is: ",max([i for i in num if i%2!=0]))
    

#enter a number: 1
#enter a number: 2
#enter a number: 3
#enter a number: 4
#enter a number: 5
#enter a number: 6
#enter a number: 7
#enter a number: 8
#enter a number: 9
#enter a number: 10
#numbers are:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#largest odd number is:  9