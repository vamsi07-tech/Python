class Employee:
    name = "Vamsi"
    language = "Python" # This is a class attribute
    salary = 1000

harry = Employee()
harry.name = "Harry" 
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here 'name' is object attribute and salary and language and attributes as they directly belong to the class