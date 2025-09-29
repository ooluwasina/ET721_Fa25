"""
Daniel Oluwasina
Lab 7, accessing data in a file

"""   
def testing():
    print("Daniel Oluwasina")

def read_data(filename):
    fileuser = open(filename, 'r')

    for each in fileuser:
        print(each)