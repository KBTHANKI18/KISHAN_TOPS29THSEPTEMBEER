#Q-19 How Do You Handle Exceptions With Try/Except/Finally In Python?Explain with coding snippets. 
#Q-19 
"""
try:
        exception code
    except:
            statement
    else:
            without exception
    finally:
            it always occurs
"""
# example:
try:
# variable definition
    a=10
    b=20
    ans=a+b
    print(ans)
except:
    print("invalid input")
else:
    print("Welcome to math world")
    # it always execute exception occurs or not
finally:
    print("THANK YOU FOR USING THIS APPLICATION")

