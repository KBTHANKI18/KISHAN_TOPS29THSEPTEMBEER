# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
def unique_list(lst):
    return list(set(lst))
my_list = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7 , 8, 8, 9, 9, 10]
print(unique_list(my_list))  
