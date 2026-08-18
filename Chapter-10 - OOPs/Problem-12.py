''' Create a class ‘Employeeʼ and add salary and increment properties to it. Write a method
‘salaryAfterIncrementʼ method with a @property decorator with a setter which changes
the value of increment based on the salary.'''

class Employee:
    salary = 50000
    increament = 10
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increament)/100
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary-self.salary)/self.salary)*100


e = Employee()
print(f"Salary = {e.salary}")
print(f"Increament = {e.increament}")
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 70000
print(e.increament)