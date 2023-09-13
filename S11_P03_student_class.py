
class Student:
    def __init__(self,name) -> None:
        self.name = name
        print(name,"is created",self)
    
    def result(self,mark):
        if mark>33:
            print(self.name," party de")
        else:
            print("chal besie..")


x = Student("Heena")
x.result(81)

# create 3 entity class
# create faculty salary status
# create grade status