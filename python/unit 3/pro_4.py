class Outer:
    def __init__(self, value):
        self.value = value
        self.inner = self.Inner()

    def show(self):
        print(f"Outer Value: {self.value}")
        self.inner.display()

    class Inner:
        def display(self):
            print("Inner Class Method Called")

o = Outer(10)
o.show()


# Output:
# Outer Value: 10
# Inner Class Method Called
