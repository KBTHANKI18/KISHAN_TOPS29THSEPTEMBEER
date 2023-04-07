"""
Abstraction : to abstract something 
              to hide implementation
for abstraction we have to import ABC class

abstract class which contain one or more abstract methods is called abstract class

what is meaning of abstract method:
which is represent only few information not allocated background information

syntax:
from abc import ABC
# ABC :Abstract Base Class

polymorphism : one class derived properties of another class 
               poly means many and morphism means form
               polymorphism which override methods
               there are 2 types of polymorphism
               (1)method overloading
               (2)method overriding

method overloading : one class have same name method property but different arguments
method overriding : one or two class have same name properties               

Note : Python does not supprt method overloading.
"""
from abc import ABC,abstractmethod
#inheritance ABC - Abstract Base Class
class RBI(ABC):
    def roi(self):
        pass

class SBI(RBI):
    def roi(self):
        return 8.5
    
class CBI(ABC):
    def roi(self):
        return 6.5
        
obj = SBI()
print(obj.roi())

obj = CBI()
print(obj.roi())