#Q-28 What relationship is appropriate for Course and Faculty? 
#A-28
class faculty:
    # setter method 
    def setId(self,id):
        self.id=id
    # getter method 
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setTechnology(self,technology):
        self.technology=technology
    def getTechnology(self):
        return self.technology
obj=faculty()
# set data
id=int(input("enter id : "))
obj.setId(id)
# get id using getter method 
print(obj.getId())
# set name - using setter
name=input("enter name: ")
obj.setName(name)
# get data
print(obj.getName())
course=input("enter course: ")
obj.setTechnology(course)
print(obj.getcourse())