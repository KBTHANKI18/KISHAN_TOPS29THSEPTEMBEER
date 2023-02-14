"""
a= 54
b = 47
print("*"*33)
print("Addition : ",(a+b))
print("Subtraction : ",(a-b))
print("Multiplication : ",(a*b))
print("Division : ",(a/b))
print("*"*33)

a = int(input("Enter the Value : "))
print(type(a)) 

a = int(input("Enter Value of A : "))
b = int(input("Enter Value of B : "))         

print("*"*33)
print("Addition : ",(a+b))
print("Subtraction : ",(a-b))
print("Multiplication : ",(a*b))
print("Division : ",(a/b))
print("*"*33)
"""

a = int(input("Enter A : "))
b = int(input("Enter B : "))
print("Before Swapping  A = ",a,",B = ",b)
"""
t = a
a = b
b =t
"""
a,b =b,a
print("After Swapping A = ",a,",B = ",b)
