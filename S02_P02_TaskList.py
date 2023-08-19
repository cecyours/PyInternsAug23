
size = int(input("Enter the size : "))

names = []

for i in range(size):
    data = input("Enter your name : ")
    names.append(data)


# display all name
for i in names:
    print(i[::-1])
    
print(names)