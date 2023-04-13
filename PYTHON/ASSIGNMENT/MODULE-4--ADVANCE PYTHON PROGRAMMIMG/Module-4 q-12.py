#Q-12 QWrite a Python program to copy the contents of a file to another file. 
#A-12
# taking two files
file1 = "myfile.txt"
file2 = "mynewfile.txt"
with open(file1, "r") as file1, open(file2, "w") as file2:
    file2.write(file1.read())
# content copied from one file to the another file
print("done successfully!!")
