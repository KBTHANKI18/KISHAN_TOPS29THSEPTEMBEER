"""
class student:
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
    
obj = student()

#set data
id = int(input("Enter id : "))
obj.setId(id)

#get id using getter method
print(obj.getId())

#set name - using setter
name = input("Enter Name : ")
obj.setName(name)

#get data
print(obj.getName())
"""

#product name class
class Product:
    #constructor
    def __init__(self):
        self.__mobile = 15000 #private
        self.laptop = 60000

    #display method
    def display(self):
        print("mobile = ",self.__mobile)
        print("laptop = ",self.laptop)

    #data change using method
    def changeData(self,mobileNewPrice):
        self.__mobile = mobileNewPrice    

#object
obj = Product()
obj.display()

#change mobile and laptop price
obj.__mobile = 18000
obj.laptop = 70000

obj.display()

print("change data using method")

#change method
obj.changeData(19000)
obj.display()


              