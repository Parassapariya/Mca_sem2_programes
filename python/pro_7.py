#list oprations

def list_methods(value):
    lenn = [1, 2, 3, 4, 5,5]
    obj = {
        'length': len(lenn),
        'max': max(lenn),
        'list': list(),
        'append': lenn.append(6),
        'count': lenn.count(5),
        'extend': lenn.extend([7, 8, 9, 10]),
        'index': lenn.index(2),
        'insert': lenn.insert(2, 11),
        'pop': lenn.pop(),
        'remove': lenn.remove(11),
        'reverse': lenn.reverse(),
        'sort': lenn.sort()
    }
    return obj.get(value, "Value is something else")

# Usage
print("length is :-",list_methods('length'))
print("max is :-",list_methods('max'))
print("list is :-",list_methods('list'))
print("append is :-",list_methods('append'))
print("count is :-",list_methods('count'))
print("extend is :-",list_methods('extend'))
print("index is :-",list_methods('index'))
print("insert is :-",list_methods('insert'))
print("pop is :-",list_methods('pop'))
print("remove is :-",list_methods('remove'))
print("reverse is :-",list_methods('reverse'))
print("sort is :-",list_methods('sort'))


