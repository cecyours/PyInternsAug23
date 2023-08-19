import random
import clrprint as clr
import time

# clr.clrprint("\u2764"*100,clr="purple")

clsList = ["red","green","magenta","yellow","magenta"]
codes = ["\u2764","\u2703","\u0407","\u8304","\u7779"]
# print(clr.clrhelp())
while True:
    time.sleep(0.001)
    x = random.choice(clsList)
    clr.clrprint(random.choice(codes),clr=x,end=" ")