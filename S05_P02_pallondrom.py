
# pallondrome numbers..
# digit seperate

x =  int(input("Enter the value : "))
# 561
reverse = 0
print("{:1} | {:5} | {:5}".format('r','num','reverse'));

orginal_num = x;

while x>0:
    digit = x%10
    reverse = reverse*10+digit
    print("{:1} | {:5} | {:5}".format(digit,x,reverse));
    x = x//10

print("------")

if orginal_num==reverse:
    print("num is pallondrom")
else:
    print("not pallondrom")