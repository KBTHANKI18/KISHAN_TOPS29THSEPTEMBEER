#  Write a Python program to check whether a list contains a sub list
def check_sublist(lst, sublist):
    lst_str = str(lst)
    sublist_str = str(sublist)
    if sublist_str in lst_str:
        return True
    else:
        return False
my_list = [1, 2, 3, 4, 5, [6, 7, 8], 9, 10]
sub_list = [6, 7, 8]
contains_sublist = check_sublist(my_list, sub_list)
print(contains_sublist)  
