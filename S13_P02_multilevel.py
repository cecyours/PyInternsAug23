
# multilevel
# A -> B -> C

class A:
   def display(self):
      print("A : i am ",self)

class B(A):
   def display(self):
      print("B : i am ",self)

class C(B):
  def display(self):
      print("C : i am ",self)



c = C()
c.display()