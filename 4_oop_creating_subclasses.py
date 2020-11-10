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
        """ Prints the full name of an Employee instance. """
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Create subclasses

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # passes first/last/pay to Employee's __init__ method to handle these initializations
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# NOTES:

# SUBCLASSES
#   Inheritance allows us to inherit attributes/methods into subclasses
#   can add new functionality without affecting parent class in any way

# Create different types of employees: Developers & Managers

dev_1 = Developer('Elliot', 'Wilens', 100000, 'Python')
dev_2 = Developer('Megan', 'Harpell', 125000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# Very helpful way to understand class inheritance if you need more info about certain class (HELP)
# print(help(Developer))

# attribute values are first taken from the instance's class, then by it's parent class(es), then by the built-in python class methods
# dev_1.apply_raise() # raise amount for dev class set to 1.10
# mgr_1.apply_raise() # no raise amount set for mgr class, so it will take the Employee raise_amt attribute of 1.04

# print(dev_1.email)
# print(dev_1.prog_lang)

# Managers class
# print("Print all employees that report to mgr_1")
# mgr_1.print_emps()
# print('Add Megan')
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# print('Remove Elliot')
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# IS INSTANCE, IS SUBCLASS
# isinstance tells us whether an object is an instance of a specified class
# print(isinstance(dev_1, Developer)) # should return True
# print(isinstance(dev_1, Employee)) # should return True
# print(isinstance(dev_1, Manager)) # should return False

# issubclass tells us whether a class is a subclass of the specified class
# print(issubclass(Manager, Employee)) # should return True
# print(issubclass(Employee, Developer)) # should return False
# print(issubclass(Developer, Employee)) # should return True

