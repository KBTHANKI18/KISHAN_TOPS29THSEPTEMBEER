
# Loop : It is continously repeating the same task again and again is called a loop.

    # In Python,

    # There are 2 Loops

    # 1) while loop
    # 2) for loop

    # Every Loop will have 3 common facts

    # 1) Initialization
    # 2) Conditional
    # 3) Updation (increment/decrement)



    # a) while

    # syntax:
    #             initialization
    #             while condition:
    #                 statement
    #                 updation
# while loop
n=int(input("enter number: "))
while n>0:
    print("yes")
    n=n-1

# wap program to print nos. from 1 to 20
n = 1
while n<=20:
    print(n)
    n = n + 1

#  wap program to print sum of no. 5
n  = int(input("enter number: "))
sum=0
while n>0:
    sum=sum+n
    n=n-1
    print("sum",sum)

# for loop
# In C,C++ or Java , the syntax of for loop is

    # for(i=0;i<10;i++)
    # {
    #     statement
    # }

    # In Python the for loop syntax is changed drastically.

    # syntax :

    #         for variable-name in range(start-value,end-value,updation):
    #             statement

    #         e.g

    #             for i in range(1,10,1):
    #                 statement

    #         i -> variable-name
    #         range -> Inbuilt function in Python

    #         range() have 3 parameters

    #         1) Start Value
    #         2) End Value
    #         3) Updation   (increment/decrement)


    #     for i in range(10):
    #         print(i)
                
    # 4 Variants of For Loop.

    # - By Default the Loop will start from 0,if you do not
    # provide the start value.
    # - By Default the Incremented value is +1, if you do not
    #   provide the updation.

# 1st variant
for i in range(10):
    print(i)

# 2nd variant
for i in range(0,11):
    print(i)

# 3rd variant
for i in range(0,22,2):
    print(i)

# 4th variant
for i in range(22,0,-2):
    print(i)

# print sum of 10 using for loop

n=int(input("enter number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
    n=n-1
    print("sum:",sum)
