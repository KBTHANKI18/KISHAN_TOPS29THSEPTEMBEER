#user defined exception
class Oddexception(Exception):
    pass


#main program executation
#accept number from user
num = int(input("Enter number : "))

try:
    #check condition
    if num%2==0:
        print("even number")
    else:
        raise Oddexception
except Oddexception:
    print("we can't accept odd numbers")
