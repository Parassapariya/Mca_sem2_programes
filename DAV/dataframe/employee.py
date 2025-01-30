import pandas as pd

data = {
    'Name': ['Raj', 'Ravi', 'Anita', 'Sara', 'John', 'Rahul', 'Mona', 'Ramesh'],
    'Age': [25, 30, 22, 29, 28, 35, 24, 32],
    'Salary': [23000, 21000, 25000, 19000, 22000, 26000, 24000, 20000],
    'City': ['Chennai', 'Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'Hyderabad', 'Kolkata', 'Chennai'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male'],
    'Dept': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'Hyderabad', 'Kolkata', 'Chennai']
}

df = pd.DataFrame(data)

print("Employees with salary > 22000:")
print(df[df['Salary'] > 22000]['Name'])

print("\nEmployees with age < 26:")
print(df[df['Age'] < 26]['Name'])

print("\nEmployees from Chennai:")
print(df[df['City'] == 'Chennai']['Name'])

print("\nEmployees with salary > 22000 (Repeated Query):")
print(df[df['Salary'] > 22000]['Name'])

print("\nEmployees whose name starts with 'R':")
print(df[df['Name'].str.startswith('R')]['Name'])

print("\nEmployees whose name ends with 'a':")
print(df[df['Name'].str.endswith('a')]['Name'])

print("\nMale employees with salary > 20000:")
print(df[(df['Salary'] > 20000) & (df['Gender'] == 'Male')]['Name'])

print("\nEmployees whose age < 30 and dept is Bangalore:")
print(df[(df['Age'] < 30) & (df['Dept'] == 'Bangalore')]['Name'])

leave_data = {
    'Name': ['Raj', 'Ravi', 'Anita', 'Sara', 'John', 'Rahul', 'Mona', 'Ramesh'],
    'Leaves_Taken': [5, 10, 3, 7, 2, 8, 6, 4]
}

leave_df = pd.DataFrame(leave_data)

merged_df = pd.merge(df, leave_df, on="Name")
print("\nMerged DataFrame:")
print(merged_df)

concat_df = pd.concat([df, leave_df], axis=1)
print("\nConcatenated DataFrame:")
print(concat_df)
