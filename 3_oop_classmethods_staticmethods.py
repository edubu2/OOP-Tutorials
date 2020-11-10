# Object-Oriented Programming tutorials from Corey Schafer's OOP YouTube Series.

class Employee:
    
    num_of_emps = 0 # will increment each time an employee is added
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@' + 'company.com'

        Employee.num_of_emps += 1 # increment num employees each time an instance is created
    
    def fullname(self):
        """ Prints the full name of an Employee instance. """
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # required for class methods
    def set_raise_amount(cls, amount):
        """ Updates the raise amount for the entire class. """
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_string):
        """ Takes employee string (ex: 'first-last-50000') and creates an employee instance.
            This is an example of an 'alternative constructor' """
        first, last, pay = employee_string.split('-')
        return cls(first, last, pay) # creates & returns the employee instance (to be assigned to a variable)

    @staticmethod
    def is_workday(day):
        """ Takes a day and returns True if day is a weekday, False otherwise. """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# What is a Class Method?
#   a method that takes in 'cls' instead of 'self' (must have @classmethod decorator)
#       can't use the word 'class' - already taken by python
#   it's a method that updates a class variable
#   

# Make sure the set_raise_amount class method works
emp_1 = Employee('Elliot', 'Wilens', 100000)
emp_2 = Employee('Megan', 'Harpell', 125000)
# print(emp_2.raise_amount)
# Employee.set_raise_amount(1.08)
# print(emp_2.raise_amount) # Great! It works.

# # Now let's say someone from HR keeps receiving new employees as a string 'fn-ln-pay'
# # Let's add a method to our class that creates a new employee, given that string instead of individual params

# emp_string = 'Brian-Urlacher-12000000'
# emp_3 = Employee.from_string(emp_string) # from_string is AKA 'alternative constructors'
# print(emp_3.last) # it works!

# # STATIC METHODS
# #   don't pass anything automatically (no 'self', no 'cls' arguments taken)
# #   does not reference the instance nor the class anywhere in the function
# # example: is_workday method

# import datetime
# my_date = datetime.date(2016, 7, 10)

# print(Employee.is_workday(my_date))