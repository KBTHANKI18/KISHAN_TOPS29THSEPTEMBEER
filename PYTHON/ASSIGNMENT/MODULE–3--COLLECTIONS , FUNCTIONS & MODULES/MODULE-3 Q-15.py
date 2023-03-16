# Write a Python program to get unique values from a list 
def unique_list(lst):
    return list(set(lst))
my_list = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7 , 8, 8, 9, 9, 10]
print(unique_list(my_list))
