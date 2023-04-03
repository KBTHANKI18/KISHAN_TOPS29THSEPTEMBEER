class faculty:
    #setter method
    def setId(self,id):
        self.id = id

    #getter method
    def getId(self):
        return self.id

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name
    
    def setTechnology(self,technology):
        self.technology = technology

    def getTechnology(self):
        return self.technology
        
obj = faculty()

#set data
id = int(input("Enter id : "))
obj.setId(id)

#get id using getter method
print(obj.getId())

name = input("Enter Name : ")
obj.setName(name)

print(obj.getName())

technology = input("Enter technology : ")
obj.setTechnology(technology)

print(obj.getTechnology())




              