#Q-22 How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 
#A-22 class: it contains data member and member function in single entity it is called class.
# syntax:     
    #  class <classname>:
    #  data member
    #  member function
# self represents current class properties
# create class of person
class person:
    # method
    def display(self):         #self represents current class properties 
        print("this is person method")
        # obj creation of person class
obj=person()
obj.display()
