"""
Daniel Oluwasina
Sept 15
Lab 5, Functions
"""

# Example one create a cunctions that passes two numbers and return the product of it
from lab5_oluwasina_functions import *

print("\n ----- Example 1: Intro Function -----")
n1 = 2
n2 = 5
p = product(n1, n2)
print(f"The prodecut of {n1} and {n2} is {p}")
p = product()
print(f"The product is {p}")
p = product(5)
print(f"The produc is {p}")

print("\n ----- Example 2: function to calculate the hypotenuse -----")

s1 = 5
s2 = 2

hyp = hypotenuse(s1, s2)

print(f"The Hypotenuse is {hyp}")

print(
    "\n ----- Example 3: Functionn to check f a number is NEGATIVE, POSITIVE, OR ZERO -----"
)

c = check_num(-3)
print(f"The number is {c}")

c = check_num(5)
print(f"The number is {c}")

c = check_num(0)
print(f"The number is {c}")

print(
    "\n ----- Example 4: Functoin that checks grades and returns true if avg over 60 -----"
)

grades = [50, 60, 80, 93]
avg = check_grades(grades)
print(f"Did i pass the class: {check_pass(avg)}")

grades = [10, 20, 50, 10]

print(f"Did i pass the class: {check_pass(check_grades(grades))}")

print("\n ----- Lab Assignment -----")
rand = rand_in_range(1, 10)

print(compare(rand))
