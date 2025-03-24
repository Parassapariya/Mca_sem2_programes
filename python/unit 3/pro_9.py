from abc import ABC, abstractmethod

class InterfaceDemo(ABC):
    @abstractmethod
    def display(self):
        pass

class Demo(InterfaceDemo):
    def display(self):
        print("Interface Method Implemented")

d = Demo()
d.display()

# Output:
# Interface Method Implemented
