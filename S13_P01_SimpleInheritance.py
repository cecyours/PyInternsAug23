

class A: # super
    def display(self):
        print("I am ",self)


class B(A): # A->B # base Class
    pass


b = B()
b.display()

a = A()
a.display()