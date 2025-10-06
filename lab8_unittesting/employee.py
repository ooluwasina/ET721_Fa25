"""
Oct 6th, 2025
unit testing
Daniel Oluwasina

"""

class Employee:
    raise_amt = 1.05

    def __init__(self,firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.sal = salary
    
    @property
    def emailemployee(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.sal = int(self.sal * self.raise_amt)



