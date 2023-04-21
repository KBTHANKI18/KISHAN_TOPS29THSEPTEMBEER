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

    elif choice == 3:
        #update data
        id = int(input("Enter Id : "))
        name = input("Enter Name : ") 
        subject = input("Enter Subject : ")

        #query
        query = "update student set name = '%s',subject = '%s' where id = %s"
        args = (name,subject,id)

        mycursor.execute(query%args)
        mydb.commit()
        print("Updated Successfully!!")

    elif choice == 4:
        #search data
        id = int(input("Enter Id : "))       

        #query
        query = "select * from student where id = %s"

        #args
        args = (id)

        mycursor.execute(query%args)
        #retrieve all data in row variable
        row = mycursor.fetchone()

        #id = 0 name = 1 subject = 2

        displayname = row[1]
        displaysubject = row[2]

        print("name = ",displayname)
        print("subject = ",displaysubject)

    elif choice == 5:
        #delete data
        id = int(input("Enter Id : "))

        #query
        query = "delete from student where id  = %s"

        #args
        args = (id) 

        mycursor.execute(query%args)

        mydb.commit()
        print("Deleted Successfully!!")



    loop_choice = input("Do you want to perform more actions press 'y' for yes and 'n' for no :") 
    if loop_choice == 'n' or loop_choice == 'no':
        status = False   
