

#
x = int(input("Enter the number : ")) # 5

# break : terminate the loop
# continue : skip the remaining part of the iteration.
for i in range(1,101):

    if i%7!=0:
        # break
        pass
        continue
    # no part to skip.
    # t   
    print(i,end = ", ")

print("....")


 
def reverse(userName):
    return int(float('29.44'));

x = reverse("GK")
print(x)

import random

def show():
    x =  int(random.random()*100)
    print("coder ",x)
    return


x = show()
print("show : ",x)

# with return

def value(x):
    return "Hi" if x=="kites" else "you"

print(value("happy"))

x = 90
result = "pass" if x>34 else "failed"
print(result)