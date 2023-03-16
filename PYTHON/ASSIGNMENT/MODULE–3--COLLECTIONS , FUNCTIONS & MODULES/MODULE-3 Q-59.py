# Write a Python program to convert degree to radian 
import math
def degree_to_radian(degrees):
    return degrees * math.pi / 180.0
degrees = 90.0
radians = degree_to_radian(degrees)
print(f"{degrees} degrees is equal to {radians:.2f} radians")
