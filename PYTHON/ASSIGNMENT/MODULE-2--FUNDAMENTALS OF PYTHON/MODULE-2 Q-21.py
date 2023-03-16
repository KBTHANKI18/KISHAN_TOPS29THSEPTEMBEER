# Write a Python function to reverses a string if its length is a multiple of 4.
def reverse_string_if_length_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]
    else:
        return input_string
input_string = "Python"
new_string = reverse_string_if_length_multiple_of_4(input_string)
print(new_string)
