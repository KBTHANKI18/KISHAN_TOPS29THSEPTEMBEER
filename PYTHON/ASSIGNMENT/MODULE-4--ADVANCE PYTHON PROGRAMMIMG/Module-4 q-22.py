#Q-21 How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 
#A-21 A class in Python can be defined using the class keyword. As per the syntax above, a class is defined using the class 
#     keyword followed by the class name and : operator after the class name, which allows you to continue in the next indented 
#     line to define class members.

#     SELF represents the instance of class. This handy keyword allows you to access variables, attributes, and methods of a defined 
#     class in Python. The self parameter doesn't have to be named “self,” as you can call it by any other name.

#     # create class
class Bike:
    name = ""
    gear = 0

# create objects of class
bike1 = Bike()