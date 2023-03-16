# Write a Python script to merge two Python dictionaries 
# To merge two Python dictionaries, update() method or the dictionary unpacking ** operator is used.
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}
dict1.update(dict2)
print(dict1)

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}
merged_dict = {**dict1, **dict2}
print(merged_dict)
