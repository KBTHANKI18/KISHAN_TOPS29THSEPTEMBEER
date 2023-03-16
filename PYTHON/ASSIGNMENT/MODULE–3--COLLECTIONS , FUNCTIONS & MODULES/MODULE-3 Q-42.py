# Write a Python program to print all unique values in a dictionary. 
my_dict = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 4, "f": 3}
unique_values = set()
for value in my_dict.values():
    unique_values.add(value)
print("Unique values:", unique_values)
