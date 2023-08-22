
n = int(input("Enter the size : "))

data = []
for i in range(0,n):
    x = int(input("Enter the number : "))
    data.append(x)

# print(data)

neg=0
pos=0
zero=0
for i in data:
    if i<0:
        neg+=1 # neg = neg + 1
    elif i>0:
        pos+=1
    else:
        zero+=1


print(data)
print(" -ve : ",neg)
print(" +ve : ",pos)
print("zero : ",zero)
