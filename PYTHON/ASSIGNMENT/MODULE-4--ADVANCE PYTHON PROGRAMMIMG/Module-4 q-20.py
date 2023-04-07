#Q-19 Write python program that user to enter only odd numbers, else willraise an exception.
#A-19 
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound