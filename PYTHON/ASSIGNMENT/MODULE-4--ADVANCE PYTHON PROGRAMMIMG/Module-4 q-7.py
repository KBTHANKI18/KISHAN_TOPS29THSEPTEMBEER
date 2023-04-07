#Q-7 Write a Python program to read a file line by line store it into a variable.
#A-7
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')