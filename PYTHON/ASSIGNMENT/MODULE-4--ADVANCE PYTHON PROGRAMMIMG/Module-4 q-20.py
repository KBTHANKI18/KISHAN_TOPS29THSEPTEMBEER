#Q-20 Write python program that user to enter only odd numbers, else willraise an exception.
#A-20 
while True:
    try:
        num = int(input("enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("Even numbers are not allowed.")
        break
    except ValueError as e:
        print(e)
