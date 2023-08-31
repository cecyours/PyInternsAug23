import array

x = array.array('i',[1,2,3,4,5,6,7,8,9,0])

for i in x[:-3]:
    print(pow(i,5),end=" ")

#array methods
x.append(100)
print(x)

x.insert(3,999)
print(x)

y = x.pop()
print(x,y)

x.remove(999) # remove object
print(x)

f = x.index(3)
print(f)
