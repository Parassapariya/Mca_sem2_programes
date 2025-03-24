class Demo:
    count = 0

    def __init__(self, value):
        self.value = value
        Demo.count += 1

    def instance_method(self):
        print(f"Instance Value: {self.value}")

    @classmethod
    def class_method(cls):
        print(f"Total Instances: {cls.count}")

d1 = Demo(10)
d2 = Demo(20)

d1.instance_method()
Demo.class_method()

# Output:
# Instance Value: 10
# Total Instances: 2