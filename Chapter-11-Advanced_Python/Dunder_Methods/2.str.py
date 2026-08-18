class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person({self.name}, {self.age})" # User-friendly

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})" # Unambiguous, for debugging

p = Person("Alice",30)
print(str(p)) 
print(repr(p)) 
print(p)