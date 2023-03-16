#  Write a Python program to replace last value of tuples in a list. 
my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_list = []
for tuple in my_list:
    new_list.append(tuple[:-1] + (10,))
print('Original list:', my_list)
print('New list:', new_list)
