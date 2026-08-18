'''Create a class ‘Petsʼ from a class ‘Animalsʼ and further create a class ‘Dogʼ from ‘Petsʼ. Add a method ‘barkʼ to class ‘Dogʼ.'''

class Animals:
    def sound (self):
        pass

class Pets(Animals):
    def __init__ (self,name):
        self.name = name

    def show(self):
        print(f"The name of the pet is {self.name}")

class Dog(Pets):
    def __init__ (self, name):
        super(). __init__ (name)

    def bark(self):
        print("Dog Barks")


            
dog = Dog("Tommy")
dog.show()
dog.bark()
