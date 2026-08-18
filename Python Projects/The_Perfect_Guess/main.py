'''We are going to write a program that generates a random number and asks the user to guess it.
If the playerʼs guess is higher than the actual number, the program displays “Lower number please” .
Similarly, if the userʼs guess is too low, the program prints “Higher number please” .
When the user guesses the correct number, the program displays the number of
guesses the player used to arrive at the number.'''

from random import randint

# User Input
def user_input():
    user = int(input("Enter a Number between 0 and 100:\n"))
    return user

# Random Number Generated
def Gen_Num():
    gen = randint(0,100)
    return gen

choice = int(input("Choose the type of difficulty:\n1:Hard 2:Medium 3:Low\n"))
if (choice == 1):
    y = 3
elif (choice == 2):
    y = 5
else:
    y = 10

# Comparison
gen = Gen_Num()
print(f"You have {y} attemps")
user = user_input()
x=0
while(x<y):
    if (user > gen):
       x += 1
       print(f"Choose a lower number. You have {y-x} chances left")
       if (y-x) == 0:
            print(f"Game Over! The correct number was {gen}")
            break
       user = user_input()
    elif (user < gen):
        x += 1
        print(f"Choose a higher number. You have {y-x} chances left")
        if (y-x) == 0:
            print(f"Game Over! The correct number was {gen}")
            break
        user = user_input()
    else:
        print(f"Correct Answer: {user}\nGussed in {x} attempts")
        break       