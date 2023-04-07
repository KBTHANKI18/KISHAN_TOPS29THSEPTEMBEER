#Q-3 Write a Python program to append text to a file and display the text. 
#A-3 open any file in specific variable 
f=open("mynewfile.txt","a")      # w- append mode
# accept value from user
name=input("enter name: ")
#using of write() write file
f.write("\n"+name)
#close file
f.close()