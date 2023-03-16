# Write a Python script to sort (ascending and descending) a dictionary by value. 
my_dict = {"apple": 5, "banana": 2, "orange": 7}
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Original dictionary:", my_dict)
print("Sorted dictionary (ascending):",asc)
print("Sorted dictionary (descending):",desc)
