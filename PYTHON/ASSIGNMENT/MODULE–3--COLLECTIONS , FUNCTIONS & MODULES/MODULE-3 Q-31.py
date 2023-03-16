#  How will you create a dictionary using tuples in python? 
#  To create a dictionary using tuples in Python, you can pass a list of tuples to the dict() constructor function. 
#  Each tuple in the list should contain exactly two elements, where the first element is the key and the second element is the value.
list = [("apple", 5), ("banana", 2), ("orange", 7)]
dict = dict(list)
print("Original list:", list)
print("Dictionary:",dict)
