#Q-7 Write a Python program to read a file line by line store it into a variable.
#A-7
# txt file
filename="myfile.txt"
# create empty string
lines=""
with open(filename, "r") as file:
    for line in file:
        lines += line
        # print lines
print(lines)