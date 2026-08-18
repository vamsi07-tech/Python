'''Create a class ‘Employeeʼ and add salary and increment properties to it. Write a method
‘salaryAfterIncrementʼ method with a @property decorator with a setter which changes
the value of increment based on the salary.'''

class Employee:
    salary = 40000
    increment = 2000

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.increment)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        return (self.increment / self.salary)*100

e= Employee()
print(e.salaryAfterIncrement)