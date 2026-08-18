class Employee:
    name = "Vamsi"
    language = "Python" # This is a class attribute
    salary = 1000

harry = Employee()
harry.language = "Java"  # This is an object attribute
print(harry.name, harry.language, harry.salary)