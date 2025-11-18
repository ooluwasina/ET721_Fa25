"""
Daniel Oluwasina
function file
Sept 15, 2025
Lab 5, function
"""

import random


# Example 1
def product(a=0, b=0):
    c = a * b
    return c


# Example 2
def hypotenuse(side1, side2):
    return (side1**2 + side2**2) ** 0.5


# Example 3
def check_num(num):
    if num > 0:
        return "POSITVE"
    elif num < 0:
        return "NEGATIVE"
    else:
        return "ZERO"


# Example 4


def check_grades(grades):
    avg = 0
    for grade in grades:
        avg += grade
    avg /= len(grades)
    return avg


def check_pass(avg_grade):
    if avg_grade >= 60:
        return True
    else:
        return False


# Lab Assingment


def rand_in_range(min, max):
    rand_num = random.randint(min, max)
    return rand_num


# print(rand_in_range(1,100))


def compare(rand):
    NUM = 7
    if rand > NUM:
        print(f"The number {rand} is bigger than the guess number {NUM}")
    elif rand < NUM:
        print(f"The number {rand} is smaller than the guess number {NUM}")
    else:
        print(f"You Got It! The number {rand} is equal to the guess number {NUM}")
