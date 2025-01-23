#list oprations

def list_methods(value):
    lenn = [1, 2, 3, 4, 5,5]
    obj = {
        '1': len(lenn),
        '2': max(lenn),
        '3': list(),
        '4': (lenn.append(6), lenn),
        '5': lenn.count(5),
        '6': lenn.extend([7, 8, 9, 10]),
        '7': lenn.index(2),
        '8': lenn.insert(2, 11),
        '9': lenn.pop(),
        '10': lenn.remove(11),
        '11': lenn.reverse(),
        '12': lenn.sort()
    }
    return obj.get(value, "Value is something else")

print("list methods")
print("1.length()\n2.max()\n3.list()\n4.append()\n5.count()\n6.extend()\n7.index()\n8.insert()\n9.pop()\n10.remove()\n11.reverse()\n12.sort()")

value = input("Enter the value: ")
# Usage
print("length is :-",list_methods(value))


