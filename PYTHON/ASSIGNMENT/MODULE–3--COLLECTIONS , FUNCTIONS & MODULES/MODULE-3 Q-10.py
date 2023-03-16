# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
def generate_list():
    squares_list = [x**2 for x in range(1, 31)]
    first_five = squares_list[:5]
    last_five = squares_list[-5:]
    result_list = first_five + last_five
    print(result_list)
generate_list()
