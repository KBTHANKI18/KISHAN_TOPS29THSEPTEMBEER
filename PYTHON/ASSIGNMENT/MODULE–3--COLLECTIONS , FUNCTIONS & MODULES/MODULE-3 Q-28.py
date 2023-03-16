#  Write a Python program to remove an empty tuple(s) from a list of tuples. 
my_list = [(1, 2), (), (3, 4), (), (5,6), ()]
new_list = [t for t in my_list if t]
print("Original list:", my_list)
print("New list:", new_list)
