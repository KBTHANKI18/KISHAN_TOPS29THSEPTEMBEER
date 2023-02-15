"""
1)POSITIVE OR NEGATIVE:
n = int(input("Enter Number : "))
if n>0:
    print("\nIt Is Positive.")
else:
    print("\nIt Is Negative.")
"""
"""
2)EVEN OR ODD:
n = int(input("Enter Number : "))
if n%2==0:
    print(n,"is Even.")
else:
    print(n,"is Odd.")
"""
"""
3)MAXIMUM:
n1 = int(input("Enter Number : "))    
n2 = int(input("Enter Number : "))
if n1>n2:
    print(n1,"is Max.")
else:
    print(n2,"is Max.")
"""
"""
4)WHICH IS GREATER.
n1 = int(input("Enter A : "))
n2 = int(input("Enter B : "))
n3 = int(input("Enter C : "))
print("A = ",n1,"B = ",n2,"C = ",n3)         
if n1>n2:
    if n1>n3:
        print(n1," is Greater.")
    else:
        print(n3," is Greater.")

else:
    if n2>n3:
       print(n2," is Greater.")
    else:
       print(n3," is Greater.")
"""
roll = int(input("Enter roll no : "))
name = input("Enter Name : ")
p = int(input("Enter Physics Marks : "))
c = int(input("Enter Chemistry Marks : "))
m = int(input("Enter Maths Marks : "))
total = (p+c+m)
per = (total/3)

print("*"*80)
print()
print("ROll NO : ",roll)
print("NAME : ",name)
print("TOTAL : ",total)
print("PERCENTAGE : ",per)

if per>75:
    print("Class IS Distinction.")
elif per>60:
    print("First Class.")
elif per>45:
    print("Second Class.")
elif per>=30:
    print("Pass Class.")
else:
    print("Fail!.")


















         
