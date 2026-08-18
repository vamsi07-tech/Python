'''Add a static method in problem 2, to greet the user with hello. '''

class Calculator:
    def __init__(self, num):
        self.num = num
        print("Hello")

    def square(self):
       print(f"Square of {self.num} = {self.num*self.num}")

    def cube(self):
           print(f"Cube of {self.num} = {self.num*self.num*self.num}")

    def sqrt(self):
           print(f"Sqrt of {self.num} = {self.num**1/2}")


a = Calculator(4)
a.square()
a.cube()
a.sqrt()