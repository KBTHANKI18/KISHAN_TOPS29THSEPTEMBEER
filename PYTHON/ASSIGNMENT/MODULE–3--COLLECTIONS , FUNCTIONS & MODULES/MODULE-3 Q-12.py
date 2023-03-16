# Write a Python program to convert a list of characters into a string.
def list_to_string(char_list):
    string = ''.join(char_list)
    return string
my_list = ['H', 'e', 'l', 'l', 'o',' ', 'W', 'o', 'r', 'l', 'd', '!']
string = list_to_string(my_list)
print(string)  
