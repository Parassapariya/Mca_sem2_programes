class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def show(self):
        print(self.value)

n1 = Number(10)
n2 = Number(5)

n3 = n1 + n2
n4 = n1 - n2

n3.show()
n4.show()

# Output:
# 15
# 5
