# Write a Python function that takes two lists and returns true if they have at least one common member.
def has_common_member(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
list3 = [10,11,12,13]
print(has_common_member(list1, list2))  
print(has_common_member(list1, list3))  
