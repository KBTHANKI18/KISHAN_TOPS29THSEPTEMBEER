#Single Level Inheritance
"""
class Parent:
    def home(self):
        print("Ahmedabad")

class Child(Parent): #inheritance
    def car (self):
        print("I Have Car") 

#object declaration
obj = Child()
obj.home()
obj.car()
"""
#Multi Level Inheritance               
"""
class Grandparent:
    def land(Self):
        print("Land in Gujarat")

class Parent(Grandparent):
    def home(self):
        print("Home at Ahmedabad")   

class Child(Parent):
    def car(self):
        print("Purchase Own Car")

#object declaration
obj = Child()

obj.land()
obj.home()
obj.car()
"""
#Multiple Inheritance
"""
A             B
|             |
---------------
       |
       v
       C
"""
"""
# parent class
class A:
    def displayA(self):
        self.num1=10
# parent class
class B:
    def displayB(self):
        self.num2=20
# multiple inheritance
class C(A,B):
    def displayRes(self):
        ans=self.num1+self.num2
        print("num1= ",self.num1)
        print("num1= ",self.num2)
        print("ans= ",ans)
obj=C()
obj.displayA()
obj.displayB()
obj.displayRes()
"""

#Hierarchical inheritance
"""
       A
       |
---------------
B             C       
"""
"""
#parent class
class parent:
    def home(self):
        print("Ahmedabad")
class Child1(parent):    #ineritance
    def car(self):
        print("I HAVE CAR")
        # obj declaration
class Child2(parent):    #ineritance
    def bike(self):
        print("I HAVE BIKE")
          # obj declaration
obj1 = Child1()
obj2= Child2()
obj1.home()
obj1.car()
obj2.home()
obj2.bike()
"""

#Hybrid Inheritance
"""
       A
       |
---------------
B             C 
---------------
       |
       D
"""
"""
# parent class
class parent:
    def home(self):
        print("Ahmedabad")
class Child1(parent):    #ineritance
    def car(self):
        print("I HAVE CAR")
        # obj declaration
class Child2(parent):    #ineritance
    def bike(self):
        print("I HAVE BIKE")
class Child3(Child1,Child2):    #ineritance
    def bike(self):
        print("WOOHOO")
          # obj declaration
obj = Child3()
obj.home()
obj.car()
"""




























