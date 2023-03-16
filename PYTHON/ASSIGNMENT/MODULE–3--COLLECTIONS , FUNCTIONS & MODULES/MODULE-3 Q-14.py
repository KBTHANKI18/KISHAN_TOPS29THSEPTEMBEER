# Write a Python program to find the second smallest number in a list.
def second_smallest(lst):
    smallest = min(lst)
    new_lst = [x for x in lst if x != smallest]
    second_smallest = min(new_lst)
    return second_smallest
my_list = [1,4,5,6,7,8,9,10]
second_min = second_smallest(my_list)
print(second_min) 
