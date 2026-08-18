''' Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects.'''

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        print("Welcome")

    def book(slf, fro, to):
        print(f"Ticket is booked from {fro} to {to} for train no. {slf.trainNo}")
        
    def status(slf):
        print(f"Train no. {slf.trainNo} is running on time")

    def fare(slf, fro, to):
        print(f"The ticket fare of train no. {slf.trainNo} from {fro} to {to} is {randint(250,500)}")    


t = Train(11225)
t.book("Hyd", "Mys")
t.status()
t.fare("Hyd", "Mys")