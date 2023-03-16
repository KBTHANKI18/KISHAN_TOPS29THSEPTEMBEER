# Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))
lst = [1, 2, 3, 2, 4, 5, 1, 3]
new_list = remove_duplicates(lst)
print(new_list)  
