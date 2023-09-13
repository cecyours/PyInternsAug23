
stu_list = ["mohan","rupesh","Neha","krishu"]


# alias : rename
my_list = stu_list
my_list[1] = "heena"

print(stu_list)
print(my_list)


# clone
your_list = stu_list[::]
your_list[1]="Jiya"

print(stu_list)
print(your_list)