'''Write a class ‘Complexʼ to represent complex numbers, along with overloaded operators
‘+ʼ and ‘*ʼ which adds and multiplies them.'''

class Complex:
    def __init__(self,x,y):
       self.x = x           # Real part
       self.y = y           # Imaginary part

    def __add__ (self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self,other):
        real = self.x * other.x - self.y * other.y
        imag = self.x * other.y + self.y * other.x
        return Complex(real, imag)

        def __str__(self):
            return f"{self.x} + {self.y}i"    
        
V1 = Complex(1,2)
V2 = Complex(3,4)
V3 = V1 + V2
print(V3)
V3 = V1 * V2
print(V3)        