# Object-Oriented Programming tutorials from Corey Schafer's OOP YouTube Series.

class Employee:
    
    num_of_emps = 0 # will increment each time an employee is added
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'company.com'

        Employee.num_of_emps += 1 # increment num employees each time an instance is created
    
    def fullname(self):
        """ Prints the full name of an Employee instance. """
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



# What is a class variable?
#   Something that's the same across all instances (example: raise amount)
#   See apply_raise(self) function
#       when we reference raise_amount in this function, we could use self.raise_amount OR Employee.raise_amount
#           there is a difference!
#               self.raise_amount: Will apply the raise_amount variable from this INSTANCE (so if that employee has a different raise_amount than the class, it will be used)
#               Employee.raise_amount: Regardless of the instance's raise_amount, the class attribute raise_amount value will be used

emp_1 = Employee('Elliot', 'Wilens', 100000)
emp_2 = Employee('Megan', 'Harpell', 125000)

print(emp_1.raise_amount)
print(emp_1.pay)

emp_1.apply_raise()

print(emp_1.pay)

emp_1.raise_amount = 1.10

print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)