"""
#factorial number:
#5 = 120
#5 = 5*4*3*2*1
#take one variable which conatin 1 value
f = 1

#accept number from user
num=int(input("Enter your num : "))

#continous multiply num with f value
for i in range(1,num+1):#num = 5 (1,6)
    f *=i #1 *=1 #1 *=2 #1*=3 #1 *=4 #1 *=5
print(f)
"""
"""
#pip : python index package
import instaloader

name = input("Enter instagram username: ")
insta = instaloader.Instaloader()

insta.download_profile(name,profile_pic_only=True)
"""

"""
import math
#accept number from user
num = int(input("Enter your num : "))

f = math.factorial(num)
print(f)
"""
"""
import math
print(math.sqrt(64))
print(math.pow(2,50))
print(math.pi)
print( math.ceil(75.88))
print(math.floor(75.55))
"""
"""
from datetime import date

mydate = date(2023,3,23)
print("date = ",mydate)
"""
"""
from datetime import date

current_date = date.today()
print("Current date = ",current_date)

print(current_date.year)
print(current_date.month)
print(current_date.day)
"""
"""
from datetime import time


t = time(10,20,30)
print(t)
"""
"""
import random
n = random.randint(1,10)
print(n)

subject = ("c","c++","java","python","css")
print(subject)
"""
"""
import platform

print(platform.architecture())
print(platform.python_version())
print(platform.machine())
print(platform.processor())
"""