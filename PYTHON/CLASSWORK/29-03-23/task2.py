# accept two nos. from the user and raise exception one first no. smaller than second
# # create class which inheriate exception
# # user defined exception
class smallerException(Exception):
    pass
# # main program execution
# # accept no. from the user
n1=int(input("enter no.1 : "))
n2=int(input("enter no.2 : "))
try:
    # check condition
    if n1>n2:
        print("n1 is greater than n2")
    else:
        # raise exception
        raise smallerException
except smallerException:
    print("first number is smaller than second")
