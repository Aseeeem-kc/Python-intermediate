"""
Introduction:
This file demonstrates the use of property decorators in Python to manage 
attribute access and manipulation in a class. Decorators provide a 
convenient way to define methods that act like attributes, allowing for 
controlled access to class data.
"""

class Employee:

    # Class variable for raise amount, which can be used to calculate salary raises.
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        """
        Initialize an Employee object with first name, last name, and pay.
        
        :param first: First name of the employee.
        :param last: Last name of the employee.
        :param pay: Salary of the employee.
        """
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """
        Property to get the email address of the employee.
        
        :return: The email address formatted as 'first.last@email.com'.
        """
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        """
        Property to get the full name of the employee.
        
        :return: The full name formatted as 'first last'.
        """
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        """
        Setter for the fullname property. Allows setting the full name by 
        splitting the name into first and last names.
        
        :param name: Full name to be set.
        """
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """
        Deleter for the fullname property. Resets first and last names to None 
        and prints a message indicating deletion.
        """
        print('Delete name!')
        self.first = None
        self.last = None

# Example Usage:
emp1 = Employee('ashim', 'kc', 69000)  # Create an Employee object with initial values.
emp1.fullname = 'aseeeeem kc'  
print(emp1.pay)  
print(emp1.email) 
print(emp1.fullname)  

del emp1.fullname  
print(emp1.email) 
