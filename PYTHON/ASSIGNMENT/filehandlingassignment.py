#Q-1 What is File function in python? What is keywords to create and write file
#A-1 Python file object provides methods and attributes to access and manipulate files. Using file objects, we can read or write
#    any files. Whenever we open a file to perform any operations on it, Python returns a file object.
# we can create, read and write file using python
# there are 4 modes in python file handling 
# r : read mode
# w : write mode
# x : create mode
# a : append mode

#Q-2 Write a Python program to read an entire text file
#A-2 take one variable which opens file 
f=open("myfile.txt","r")
print(f.read())

#Q-3 Write a Python program to append text to a file and display the text. 
#A-3 open any file in specific variable 
f=open("mynewfile.txt","a")      # w- append mode
# accept value from user
name=input("enter name: ")
# using of write() write file
f.write("\n"+name)
# close file
f.close()

#Q-4 Write a Python program to read first n lines of a file.
#A-4 accept line from the user
n = int(input("\n\t\tEnter Lines To Read : "))
# open any file in specific variable 
f = open("myfile.txt","r")
# use for loop
for i in range(n):
	# read line
	print(f.readline())

#Q-5 Write a Python program to read last n lines of a file.
#A-5 accept line from the user
n = int(input("\n\t\tEnter Lines To Read : "))
# open any file in specific variable 
f = open("myfile.txt","r")
# use for loop
for i in range(n):
	# read line
	print(f.readline())