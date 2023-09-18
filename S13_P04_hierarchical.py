
# A -> C
# B -> C

class A:
    def display(self):
        print("A i am ",self)

class B:
    def display(self):
        print("B i am ",self)

class C(B,A):
    pass

c = C()

c.display()

# print(C.__mro__)
for  i in C.__mro__[::-1]:
    print(i)
