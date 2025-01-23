def match_case(value):
    num1=input("Enter Number 1:")
    num2=input("Enter Number 2:")  
    match value:
        case 1:
            return "It's one"
        case 2 | 3:
            return "It's two or three"
        case _:
            return "Something else"

print(match_case(1)) 
print(match_case(3))  
