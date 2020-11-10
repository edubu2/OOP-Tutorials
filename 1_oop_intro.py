# Object-Oriented Programming tutorials from Corey Schafer's OOP YouTube Series.
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'company.com'
    
    def fullname(self):
        """ Prints the full name of an Employee instance. """
        return "{} {}".format(self.first, self.last)

emp_1 = Employee('Elliot', 'Wilens', 100000)
emp_2 = Employee('Megan', 'Harpell', 125000)

print(emp_1.fullname())