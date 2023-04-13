#Q-11 Write a Python program to write a list to a file. 
#A-11
# creating the list
my_list = ["apple", "banana", "orange", "mango"]
filename = "my_list.txt"
with open(filename, "w") as file:
    for item in my_list:
        file.write(item + "\n")
# print list to the file
print("done successfully!!")
 
