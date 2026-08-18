'''Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute?'''

class demo:
    a = 5

o = demo
print(o.a)
o.a = 10
print(o.a)

# Yes this doesn't change the class attribute