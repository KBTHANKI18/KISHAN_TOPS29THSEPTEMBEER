# Write a Python program to check a list is empty or not.
def is_list_empty(lst):
    if not lst:
        return True
    else:
        return False
lst1 = []
lst2 = [1, 2, 3]
print(is_list_empty(lst1))  
print(is_list_empty(lst2))  
