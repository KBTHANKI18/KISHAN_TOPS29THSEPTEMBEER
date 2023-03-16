# Write a Python function to check whether a number is in a given range.
def check_range(number, range_tuple):
    return range_tuple[0] <= number <= range_tuple[1]
def test_range(n):
    if n in range(10,20):
        print( "Number %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(15)
