#  Write a Python program to find the highest 3 values in a dictionary.
my_dict = {"a": 10, "b": 5, "c": 20, "d": 15, "e": 30}
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
highest_values = [value for key, value in sorted_dict[:3]]
print("The highest 3 values in the dictionary are:", highest_values)
