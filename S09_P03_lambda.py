

def sum(x, y): return x+y


kites = sum(9, -9)
print(kites)


def max(x, y): return x if x > y else y


print(max(kites, 10))


list = [1, 2, 3, 4, 5, 16, 7, 8, 9, 0]
s = map(lambda x: x*2, list)
print(tuple(s), s)

s = filter(lambda x: x % 2 == 0, list)

print(tuple(s))

# scope of Variable
""" 
    - local 
    - global
 """
# Recursion
""" 
    - base case in recusion
    - advantage & disadvantages 
 """
# Modules
""" 
    - creating used-defined module
    - importing modules
    - \__main__
    - use modules in other program

 """
