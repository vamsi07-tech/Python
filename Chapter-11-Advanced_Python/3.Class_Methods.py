class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

string = "John-2000"
e1 = Employee.fromstr(string)
print(e1.name)
print(e1.salary)