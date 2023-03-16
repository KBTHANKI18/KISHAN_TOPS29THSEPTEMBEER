# Write a Python program to unzip a list of tuples into individual lists.
my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*my_list)
print("Original list:", my_list)
print("Numbers:", numbers)
print("Letters:", letters)
