# Object-Oriented Programming tutorials from Corey Schafer's OOP YouTube Series.
class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        """ Returns the email address. """
        return "{}.{}@company.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        """ Returns the full name of an Employee instance. """
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        """ Takes the name we will use to update the first & last name when a user updates the 'fullname' attribute in their code.
            NOTE: this would require some regex in a real-world example, as first and last names may have spaces. """

        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
    """ Customize what happens when user calls 'rem <instance>.fullname'
        In this case, it will print 'Delete Name!' to screen & update first/last to None. """

        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Elliot', 'Wilens')

# PROPERTY DECORATORS
#   Used to be able to access a method like an attribute (i.e. without '()')

# Why are property decorators needed? (Assume that there is still 'email' attr. of Emp class at this point)
# print Elliot's fullname & email:
# print(emp_1.fullname()) # Elliot Wilens
# print(emp_1.email) # Elliot.Wilens@company.com

# update Elliot's first name to Eli
emp_1.first = 'Eli'

# again, print Eli's full name and email:
print(emp_1.fullname)
print(emp_1.email) # UH OH! THE FIRST NAME DIDN'T UPDATE IN THE EMAIL ADDRESS.

# The people using our classes need this to update the email address as well, so we need to fix it.

# Solution: move email attribute into a method?
# yes, this works, but then we need to call email as a function (with '()') rather than an attribute.
#   this is not ideal. People would have to change their code and it would break stuff!
# We need a way to access this function like a method, SO WE NEED THE PROPERTY DECORATOR!

# SETTER

emp_1.fullname = 'Elliot Wilens'
print(emp_1.fullname)
print(emp_1.email)