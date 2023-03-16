# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
def get_string(string):
    if len(string) < 2:
        return ''
    else:
        return string[:2] + string[-2:]
print(get_string('Hello World'))
print(get_string('Hi'))  
print(get_string('A')) 

