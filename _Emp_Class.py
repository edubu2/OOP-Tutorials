# Object-Oriented Programming tutorials from Corey Schafer's OOP YouTube Series.

# Summary of Tutorials:

class Employee:
    
    num_of_emps = 0 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)

        Employee.num_of_emps += 1 
    
    @property
    def email(self):
        """ Returns the email address (as an attribute). """
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        """ Returns the full name of an Employee instance (as an attribute). """
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