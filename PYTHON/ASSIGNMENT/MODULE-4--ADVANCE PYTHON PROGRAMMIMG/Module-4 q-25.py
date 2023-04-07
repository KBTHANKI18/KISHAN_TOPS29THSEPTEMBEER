#Q-24 Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
#A-24
"""
#     Inheritance relationship defines the classes that inherit from other classes as derived, subclass, or sub-type classes.
#A Python program to demonstrate inheritance 
class Person(object):
   
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
 
 
# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()
"""

"""
#     The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach. 
#     The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize
#     the object's attributes and serves no other purpose. It is only used within classes.
"""
"""
#     A constructor is a unique function that gets called automatically when an object is created of a class. 
#     The main purpose of a constructor is to initialize or assign values to the data members of that class. 
#     It cannot return any value other than none.
"""
