# A -> B 
# A -> C


class A:
    def display(self):
      print("Coder : i am ",self)

class B(A):
   pass

class C(A):
   pass

b = B()
c = C()

b.display()
c.display()
