"""
Daniel Oluwasina
Sept 17, 2025
Lab 6 : objects and classes
"""

print("\n ----- Example 1: create a class ----- ")


class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def addRadius(self, r):
        self.radius += r
        return self.radius


class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return self.height * 2 + self.width * 2


# creating an instance of the class
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")


rectangle1 = Rectangle(2, 5, "magenta")
rectangle2 = Rectangle(7, 3, "blue")

# acessing inforamtion in an object
print(f"The color of circle 2 is {circle2.color}")
print(f"The width of Rectangle 1 is {rectangle1.width}")

# updating data in an object
print(f"The color of circle 1 is {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle 1  after the update is {circle1.color}")

print(f"The radius of circle2 is {circle2.radius}")
circle2.addRadius(5)

print(f"The radius of circle2 after the update is {circle2.radius}")

print(f"The area of rectangle1 is {rectangle1.area()}")
print(f"The perimeter of rectangle2 is {rectangle2.perimeter()}")


print("\n ----- Lab Exercise ----- ")


class BankAccount(object):
    def __init__(self, accountHolder, accountNumber):
        self.accountHolder = accountHolder
        self.accountNumber = accountNumber
        self.balance = 250.0

    def deposit(self, d):
        if d <= 0:
            print(f"Please deposit an amouint greater than 0")
        else:
            self.balance += d

    def withdraw(self, w):
        if w <= 0:
            print(f"Please enter a number greater than 0")
        elif w > self.balance:
            print("You cant withdraw an amount greater than your balance")
        else:
            self.balance -= w
            return self.balance


useraccount = BankAccount(123456789, "Student's name")

# Demonstrating deposits and withdrawals
useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)
# prompt result
print(f"Final balance {useraccount .balance}")
