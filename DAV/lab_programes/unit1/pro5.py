'''
Write a program to prompt users to enter their working hours
and rate per hour to calculate gross pay. The program should
give the employee 1.5 times the hours worked above 30 hours. If
Enter Hours is 50 and Enter Rate is 10, then the calculated
payment is Pay: 550.0.
'''

hr = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

if hr > 30:
    rate = rate * 1.5
    print("Gross Pay is: ", hr * rate)
else:
    print("Gross Pay is: ", hr * rate)