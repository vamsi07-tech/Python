class Employee:
    name = "Vamsi"
    language = "Python" # This is a class attribute
    salary = 1000

    def getInfo(self):
        print(f"The Language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")

harry = Employee()
harry.language = "Java"  # This is an object attribute
harry.getInfo()
harry.greet()