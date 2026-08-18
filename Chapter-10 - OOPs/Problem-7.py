'''Create a class (2-D vector) and use it to create another class representing a 3-D vector.'''

class TwoD:
    def __init__ (self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i+{self.j}j")

class ThreeD(TwoD):
    def __init__ (self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def show(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")

a = TwoD(1,2)
a.show()
b = ThreeD(3,4,5)
b.show()