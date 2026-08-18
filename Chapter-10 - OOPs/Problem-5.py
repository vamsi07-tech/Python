'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. '''

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
        print("Welcome")

    def book(self, fro, to):
        print(f"Ticket is booked from {fro} to {to} for train no. {self.trainNo}")
        
    def status(self):
        print(f"Train no. {self.trainNo} is running on time")

    def fare(self, fro, to):
        print(f"The ticket fare of train no. {self.trainNo} from {fro} to {to} is {randint(250,500)}")    


t = Train(11225)
t.book("Hyd", "Mys")
t.status()
t.fare("Hyd", "Mys")

''' 
trainNo
is a local parameter of __init__().
This:
self.trainNo
is an instance variable/attribute belonging to the object.
They happen to have the same name, but they are not the same variable.

def __init__(self, trainNo):
    self.trainNo = trainNo

Think of it as:
trainNo          → temporary input
                     ↓
self.trainNo      → stored inside object
Why aren't fro and to written as self.fro and self.to?

Because the program doesn't need to store them in the object.

The route is only needed when book() is called:

t.book("Rampur", "Delhi")

If you wanted to store the route for later use, you could do:

class Train:

    def book(self, fro, to):
        self.fro = fro
        self.to = to
'''