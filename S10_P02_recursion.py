
def display(x):
    if x==0:
        return
    print("Hi Coder... ",x)
    display(x-1);
    print(" ----- ",x)
# display(100);
i = 0
def show(name):
    global i
    if(not len(name)):
        return
    end=" "*(len(name)//2+i+i)
    print(end,end="")
    print(name[::1])
    i+=1
    show(name[1:-1])

import os
os.system("clear")
show("Computer Education & Cybernetics")
input()

""" 
1. display table of given number using recursion
2. find prime number using
3. 
 """

