'''Create a class Employee with a private attribute _salary
Use @property to define a getter for salary .
Use @salary.setter to prevent setting negative values (print a warning instead).
Create an object and test by setting positive and negative salaries.'''

class Employee:
    def __init__(self, _salary):
        self. _salary = _salary
        
    @property
    def salary(self):
        return self. _salary
        
    @salary.setter
    def salary(self, amount):
        if amount >= 0:
            self. _salary = amount
        else:
            print("Salary cannot be negative")
            

emp = Employee(50000)
emp.salary = 60000
print(emp.salary)
emp.salary = -20000
print(emp.salary)