"""
Daniel Oluwasina
Oct 15, 2025
Lab 10
"""


def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)


def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()


def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added")


# Exercise:
def email_read(filename, email):
    count_email = 0
    with open(filename, "r") as file1:
        filelines = file1.readlines()
        for eachline in filelines:
            if email in eachline:
                count_email += 1
                print(eachline.strip())
    return count_email
