#importing connecting file

import connection
import pymysql

#connect with database
mydb = pymysql.connect(host="localhost",user="root",password="",database="10feb_db")
mycursor = mydb.cursor()

status = True
while status:
    data = """
                                Menu

                                (1)store data
                                (2)view data
                                (3)update data
                                (4)search data
                                (5)delete data
         """
    
    print(data)

    choice = int(input("Enter Your Choice : "))
    if choice ==1:
        #to insert data
        name = input("Enter your Name : ") 
        subject = input("Enter Subject : ")

        #query
        query = "insert into student (name,subject) values ('%s','%s')"

        args = (name,subject)

        mycursor.execute(query % args)
        #to save changes
        mydb.commit()
        print("successfully data inserted")

    elif choice == 2:
        #to fetch all data from table
        query = "select * from student"

        #execute query
        mycursor.execute(query)
        
        #to fetch all data from query
        data = mycursor.fetchall()

        print(data)


    loop_choice = input("Do you want to perform more actions press 'y' for yes and 'n' for no :") 
    if loop_choice == 'n' or loop_choice == 'no':
        status = False   
