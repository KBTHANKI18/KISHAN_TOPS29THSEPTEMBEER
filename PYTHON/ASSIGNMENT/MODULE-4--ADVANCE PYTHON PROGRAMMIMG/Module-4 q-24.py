#Q-24 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a
#     circle
#A-24 
# import math library
import math
# create class circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
        # define area
    def area(self):
        return math.pi * (self.radius ** 2)
    # define perimeter
    def perimeter(self):
        return 2 * math.pi * self.radius
circle = Circle(5)
# print area
print(circle.area()) 
# print perimeter   
print(circle.perimeter())  

