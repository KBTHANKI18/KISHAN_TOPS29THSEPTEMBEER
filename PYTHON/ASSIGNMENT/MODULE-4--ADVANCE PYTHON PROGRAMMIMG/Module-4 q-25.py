#Q-25 Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
#A-25
# inheritance: one class derives properties of another class
#  it provides reusabilities 
#  by using of inheritance we can reduce our code
#  types:
#  1)single level inheritance
#  2)multi level inheritance
#  3)multiple inheritance
#  4)heierarchical inheritance
#  5)hybrid inheritance
# example:
class parent:
    def home(self):
        print("Ahmedabad")
class Child(parent):    #ineritance
    def car(self):
        print("I HAVE CAR")
        # obj declaration
obj = Child()
obj.home()
obj.car()
# init:
# __init__.py : it indicates any folder as a package.
# constructor is a unique function that gets called automatically when an object is created of a class.


