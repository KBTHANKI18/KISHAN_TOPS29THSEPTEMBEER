#  Write a Python program to check multiple keys exists in a dictionary .
#  Using all() function along with a list comprehension to check if multiple keys exist in a dictionary.
def check_keys(dict_obj, keys_list):
    return all(key in dict_obj for key in keys_list)
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
keys_to_check = ['name', 'city', 'country']
result = check_keys(my_dict, keys_to_check)
if result:
    print("All keys exist in the dictionary")
else:
    print("One or more keys not found in the dictionary")
