#Q-6 Write a Python program to read a file line by line and store it into a list
#A-6
# txt file
filename="myfile.txt"
# create empty list
line=[]
with open(filename, "r") as file:
    for line in file:
        line.append(line.strip())
        # print line
print(line)