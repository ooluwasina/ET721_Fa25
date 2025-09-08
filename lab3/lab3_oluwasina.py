"""
Daniel Oluwasina
Lab 3, conditional statement and loops
Sep 8, 2025

"""

# conditional statement

print("\n---Example 1 if, elif, else--- (Exercise) ")
# guess a number between 1 and 9

guess_num = 8

user_number = int(input("guess a number: "))
for n in range(2):
    if(user_number == guess_num):
        print(f"Great job, {user_number} is correct")
        break
    elif(user_number>guess_num):
        print(f"{user_number} should be lower")
        user_number = int(input("guess a number: "))
    elif(user_number<guess_num):
        print(f"{user_number} should be higher")
        user_number = int(input("guess a number: "))
    else:
        print("Error")

print(f"All out of tries")



print("\n---Example 2 logical operators--- ")

"""
Eaxample 2: 
children under the age of 9 are given milk

children from 10 to 14 are given a sandwich

children from 15 to 17 are given a burger

"""

age_student = int(input("Enter and age: "))
lunch = "none"
if age_student <= 9 and age_student>= 5:
    lunch = "milk"
elif age_student >=10 and age_student<=14:
    lunch = "sandwhich"
elif age_student >=15 and age_student<=17:
    lunch = "burger"
else:
    lunch = "none"

print(f"At age {age_student} lunch is {lunch}")

print("\n---Example 3 for loops--- ")

for n in range(3):
    print(n)

print("\n---Example 4 for loop in a list--- ")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"year {index+1} = {years[index]}")

    print("\n---Example 3 while loop as a counter--- ")

count = 1
while count<=5:
    print(count)
    count+=1

print("\n---Example 4 while loop to validate a number---")

num = int(input("Enter a number between -5 and 5: "))

while num < -5 or num >5:
    num =int(input(" ERROR! Enter a number between -5 and 5: "))