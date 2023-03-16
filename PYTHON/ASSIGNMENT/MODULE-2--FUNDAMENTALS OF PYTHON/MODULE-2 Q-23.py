# Write a Python function to insert a string in the middle of a string.
def insert_string_middle(original_string, string_to_insert):
    """Inserts a string into the middle of another string."""
    middle_index = len(original_string) // 2
    return original_string[:middle_index] + string_to_insert + original_string[middle_index:]
original_string = "Hello world"
string_to_insert = "beautiful "
new_string = insert_string_middle(original_string, string_to_insert)
print(new_string)
