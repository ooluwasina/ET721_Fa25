"""
Daniel Oluwasina
Lab 7, accessing data in a file
Oct 14, 2025
"""
from lab7_function import *

testing()
print("\n----- Example 1: Reading file -----")
read_data("phrases.txt")

print("\n----- Example 2: Read specific portion of a file -----")
read_up("phrases.txt")

print("\n----- Example 3: Read specific portion of a file using readline -----")
read_lines("phrases.txt")

print("\n----- Example 4: Read specific portion of a file using readlines-----")
read_all("phrases.txt")

print("\n----- Example 5: loop through each line-----")
read_each("phrases.txt")

print("\n----- Example 6: creating a new file-----")
new_file("oluwasina.txt")

print("\n----- Example 7: append data into an existing file-----")
stamp_date("oluwasina.txt")

print("\n----- Exrcise -----")
count_yahoo = email_read("user_email.txt", "@yahoo")
count_gmail = email_read("user_email.txt", "@gmail")
count_hotmail = email_read("user_email.txt", "@hotmail")

new_email_file("reportemail.txt", count_yahoo, count_gmail, count_hotmail)