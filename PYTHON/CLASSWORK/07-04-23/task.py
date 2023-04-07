from abc import ABC,abstractmethod
#inheritance ABC - Abstract Base Class
class vehicle(ABC):
    def wheel(self):
        print(" i have alloy wheels")
    def color(ABC):
        print("i have black colour")
        
class car(vehicle):
    def skoda(self):
        print("i have skoda")

class bike(vehicle):
    def r15(self):
        print("i have r15")

class truck(vehicle):
    def bmw(self):
        print("i have bmw truck")

obj = car()
print(obj.skoda())

obj = bike()
print(obj.r15())

obj = truck()
print(obj.bmw())