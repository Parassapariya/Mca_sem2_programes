#list oprations

def lsit_methods(value):
    lenn = [1, 2, 3, 4, 5]
    obj = {
        'length': len(lenn),
        'max': max(lenn),
    }
    return obj.get(value, "Value is something else")

# Usage
print("length is :-",lsit_methods('length'))
print("max is :-",lsit_methods('max'))

