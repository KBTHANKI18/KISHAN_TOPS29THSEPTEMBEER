# Write a Python program to calculate the area of a trapezoid 
def area_of_trapezoid(base1, base2, height):
    area = ((base1 + base2) / 2) * height
    return area
base1 = 3
base2 = 4
height = 5
area = area_of_trapezoid(base1, base2, height)
print("Area of the trapezoid is:", area)
