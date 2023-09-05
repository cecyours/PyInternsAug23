import S09_P01_Function
from S09_P01_Function import *

partition("Default agrs")
def sum(a=0,b=0):
    print (a," + ",b," = ",(a+b))

sum()
sum(10)
sum(10,9)

partition("Keyword arguments")
def sum(a,b):
    print (a," + ",b," = ",(a+b))

sum(9,3)
sum(b=3,a=5) #keyword argument

partition("arbitrary arguments")

def sum(*a):
    s = 0
    for i in a:
        s += i
    print ("sum : ",s)

sum(9,92,9,2)

def max(*a):
    m = a[0]
    for i in a:
       if i>m:
           m = i
    return m

x = max(9,2,8,7,3,7,8)
print("max : ",x)

