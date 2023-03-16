# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
def count_strings(list_of_strings):
    count = 0
    for string in list_of_strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count
list_of_strings = ['python', 'programming', 'hello', 'madam', 'world', 'list']
count = count_strings(list_of_strings)
print(count)  
