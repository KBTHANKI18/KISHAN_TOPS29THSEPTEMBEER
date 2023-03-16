# Write a Python program to calculate surface volume and area of a cylinder 
import math
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
volume = math.pi * radius ** 2 * height
print("The surface area of the cylinder is:", surface_area)
print("The volume of the cylinder is:", volume)
