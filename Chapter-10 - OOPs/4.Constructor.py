class Employee:
    name = "Vamsi"
    language = "Python" 
    salary = 1000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

harry = Employee("Harry", 1300000,"Java")
print(harry.name, harry.salary, harry.language)