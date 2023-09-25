from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        print("Bye")

    @abstractmethod
    def say(self):
        pass

class B(A):
    
    def show(self):
        pass

s = B()

s.show()