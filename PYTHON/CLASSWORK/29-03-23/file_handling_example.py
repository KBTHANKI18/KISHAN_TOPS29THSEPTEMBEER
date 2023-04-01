"""
# take one variable which opens file 
f=open("myfile.txt","r")
print(f.read())
"""

""""
with open("myfile.txt","r") as f:
 print(f.read())    
"""

""""
# open any file in specific variable 
f=open("mynewfile.txt","w")      # w- write mode
# accept value from user
name=input("enter name: ")
# using of write() write file
f.write("\n"+name)
# close file
f.close()
"""

"""
#  open any file in specific variable 
f=open("mynewfile.txt","a")      # w- append mode
# accept value from user
name=input("enter name: ")
# using of write() write file
f.write("\n"+name)
# close file
f.close()
"""

"""
# create blank file
f=open("blankfile.txt","x")
f.close()
"""