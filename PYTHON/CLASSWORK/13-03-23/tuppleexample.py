"""
List & Tupple:

both are collection data type

List: It is a mutable data type which is contain data number in single location 
      which is contain similar and dis-similar data elements at one location list
      which is represent by []

    list which is indexable,orderable,mutable(change)

Tupple: It is a collection data type.
        It is indexable,orderable,immutable(no change)    
"""
"""
t = (10,20,30)
print(type(t))
print(t)
"""
"""
t = ("python","java","android","flutter","react")
print(t)

for item in t:
    print(item)
"""
"""
t = ("python","java","android","flutter","react")
print(t)

for item in t:
    print(item,end=",")
"""
"""
t = ("python","java","android","flutter","react")
print(t)

print(len(t))    
"""
"""
import random

n = random.randint(1,100)
print(n)

l1 = ["python","java","android","flutter","react"]
print(random.choice(l1))
"""
"""
t = ("python","java","android","flutter","java")

print(t.count("java"))
"""
"""
t = ("python","java","android","flutter","java")

l1 = list(t)
l1[0] = "flutter"
t = tuple(l1)
print(t)
"""