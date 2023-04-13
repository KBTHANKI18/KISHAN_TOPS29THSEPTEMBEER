#Q-29 What relationship is appropriate for Student and Person?
#A-29 
class student:
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
obj=student()
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