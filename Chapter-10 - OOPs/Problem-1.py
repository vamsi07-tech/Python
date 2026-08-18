''' Create a class “Programmer” for storing information of few programmers 
working at Microsoft. '''

class Programmer:
    company = "Microsoft"
    def __init__(self, name, language, salary):
       self.name = name
       self.language = language 
       self.salary = salary
       print(f"{self.company}, {self.name}, {self.language}, {self.salary}")

employ1 = Programmer("Vamsi", "Python", 130000)
employ2 = Programmer("Krishna", "Java", 120000)