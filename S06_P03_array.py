
import array

x = [3,5,3,6,7,9,'3434']

x = array.array('I',[1,4,3,6,98,59,6,8,29,4,4,4,4,99,1])


i = x.count(6)
# print(i)
for i in set(x):
    print("{:3} -> {:3}".format(i,x.count(i)))