#Q-23 Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 
#A-23
# take class named rectangle
class Rectangle:
    # define init,length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width
        # define area 
    def area(self):
        return self.length * self.width
    # taking length=5,width=10
rect = Rectangle(5, 10)
# print the area of rectangle
print(rect.area())  
