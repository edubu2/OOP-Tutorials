# Object-Oriented Programming tutorials from Corey Schafer's OOP YouTube Series.

class Employee:
    
    num_of_emps = 0 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@' + 'company.com'

        Employee.num_of_emps += 1 
    
    def fullname(self):
        """Returns the employees full name, given an Employee. """
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        """Increases employee pay by the value of the raise_amount class attribute. """
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        """This method should always be there, and should return the exact string needed to create the same instance. """
        
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        """This should be more human readable for an end-user. """
        
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other_emp):
        """Customize what happens when two instances are added together.
            In this case we want to return the sum of their pays. """
        
        return self.pay + other_emp.pay

    def __len__(self):
        """Customize what happens when someone calls len(instance).
            In this case we want to return the num. characters in the employee's full name (INCLUDING SPACES).
            Could be useful if, for example, someone was creating a document and needed to know if emp name would fit on one line. """
        
        return len(self.fullname())
# NOTES

emp_1 = Employee('Elliot', 'Wilens', 100000)
emp_2 = Employee('Megan', 'Harpell', 125000)

# SPECIAL METHODS: change built-in behavior of classes
#   always surrounded by DUNDERS/double underscores ('__') AKA DUNDERS!

# 2 more common special methods that we should (probably) ALWAYS implement:
    # __repr__
    # __str__

# __repr__
#   meant to be an unambiguous representation of the object, seen by other developers
#   should be used for logging, debugging, etc.

# __str__
#   meant to be a more readable representation of the object
#   meant to be displayed to end-user
#   if there's no __str__ method defined, then it will default to __repr__

# print(emp_1) # without __self__, returns __repr__ output. Without either, returns the standard python object (yuck)
# print(repr(emp_1))
# print(str(emp_1))

# # The above two lines are the same as calling:

# print(emp_1.__repr__())
# print(emp_1.__str__())

# # OTHER SPECIAL METHODS: DUNDER ADD
# #   allows us to customize what happens when we add two instances together
# #   in our class, we had it return the salaries
# print(emp_1 + emp_2)

# # __LEN__ dunder method
# print(len(emp_1)) # 'test' is an instance of class:str. __len__ is a special method within class:str. 
#     # we can define a __len__ method to customize what happens when __len__ is called on our classes.