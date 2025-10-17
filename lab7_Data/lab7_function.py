"""
Daniel Oluwasina
Lab 7, accessing data in a file
Oct 14, 2025
"""   
def testing():
    print("Daniel Oluwasina")
#Example 1: read file
def read_data(filename):
    with open(filename, 'r') as file1:
        filecontent = file1.read()
        print(filecontent)

    print(f"Is this closed?{file1.closed}")
#Example 2: reading specific portion of a file
def read_up(filename):
    with open(filename, 'r') as file1:
        #read first 30 char
        print(file1.read(30))
        #read the next 5 char
        print(file1.read(5))
#Example 3: readline
def read_lines(filename):
    with open(filename, 'r') as file1:
        print(file1.readline(30))
        print(file1.readline(5))
#Example 4: readlines
def read_all(filename):
    with open(filename, 'r') as file1:
        print(file1.readlines())
#Example 5: loop though readlines
def read_each(filename):
    with open(filename, 'r') as file1:
        filelines = file1.readlines()
        for eachline in filelines:
            print(eachline.strip())
#Example 6: create a new file
def new_file(filename):
    with open(filename, 'w') as file:
        file.write("Python Basics for Data Analiysis")
        file.write("\nDaniel Oluwasina")
#Example 7: Append data into an existing file
from datetime import datetime
def stamp_date(filename):
    with open(filename, 'a') as file:
        file.write(f"\n\n{datetime.now()}")
#Exercise:
def email_read(filename, email):
    count_email = 0
    with open(filename, 'r') as file1:
        filelines = file1.readlines()
        for eachline in filelines:
            if email in eachline:
                count_email+=1
                print(eachline.strip())
                          
    return count_email 
def new_email_file(filename, yahoo, gmail, hotmail):
    with open(filename, 'w') as file:
        file.write(f"\nyahoo = {yahoo}")
        file.write(f"\ngmail = {gmail}")
        file.write(f"\nhotmail = {hotmail}")

