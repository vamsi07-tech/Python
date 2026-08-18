class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the company is {self.company} and the salary of the employee is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name of the company is {self.company} and the salary of the employee is {self.salary}")

a = Employee()
b = Programmer()
a.salary = 1000
b.salary = 2000
a.show()
b.showLanguage()
print(a.company)
print(b.company)