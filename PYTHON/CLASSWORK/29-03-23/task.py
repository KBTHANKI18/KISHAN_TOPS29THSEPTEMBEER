
#accept number from user raise exception if user enter below zero value.
# create class which inheriate exception
# # user defined exception
class PositiveExxception(Exception):
     pass
#main program execution
#accept no. from the user
n=int(input("enter no. : "))
try:
    # check condition
    if n>0:
        print("positive")
    else:
        # raise exception
        raise PositiveExxception
except PositiveExxception:
    print("we can't accept negative nos.")
