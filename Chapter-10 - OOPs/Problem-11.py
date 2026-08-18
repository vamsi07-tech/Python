'''Write __str__() method to print the vector as follows:
7i + 8j + 10k  Assume vector of dimension 3 for this problem.'''

class Complex:
    def __init__(self,x,y,z):
       self.x = x           # Real part
       self.y = y           # Imaginary part
       self.z = z 

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"    
        
V1 = Complex(7,8,10)
print(V1)

