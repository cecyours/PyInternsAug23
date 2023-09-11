
data = [19,64,74,88,34,88,23]

result = filter( lambda x:x>33,data)

x = list(result)
print(result, x)

for i in x:
    print("passing marks : ",i)
    


data2 = map(lambda x : x if x>33 else x+(33-x),data)

for i in list(data2):
    print(i)
