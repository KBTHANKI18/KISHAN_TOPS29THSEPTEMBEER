#Q-9 Write a Python program to count the number of lines in a text file 
#A-9
# txt file
filename = "myfile.txt"
num_lines = 0
with open(filename, "r") as file:
    for line in file:
        num_lines += 1
# print no. of lines
print("no. of lines:", num_lines)

