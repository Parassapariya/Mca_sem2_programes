from abc import ABC, abstractmethod

class AbstractDemo(ABC):
    @abstractmethod
    def show(self):
        pass

class Demo(AbstractDemo):
    def show(self):
        print("Abstract Method Implemented")

d = Demo()
d.show()

# Output:
# Abstract Method Implemented
