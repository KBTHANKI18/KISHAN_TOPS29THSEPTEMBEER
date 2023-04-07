#Q-4 Write a Python program to read first n lines of a file.
#A-4 accept line from the user
n = int(input("\n\t\tEnter Lines To Read : "))
# open any file in specific variable 
f = open("myfile.txt","r")
# use for loop
for i in range(n):
# read line
  print(f.readline())
