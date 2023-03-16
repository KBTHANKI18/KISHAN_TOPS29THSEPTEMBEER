# Write a Python program to read a random line from a file. 
import random
filename = "example.txt"
with open(filename, "r") as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line)
