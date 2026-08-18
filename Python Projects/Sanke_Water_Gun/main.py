# Computer input
# Welcome page
# User input
# Comparison logic
import random

def user_input():
    print("Welcome to Snake, Water, Gun Game")
    print("---------------------------------")
    user = input("Enter your choice: Select \n s: Snake \n w: Water \n g: Gun\n")
    return user

def computer_input():
    computer = random.choice([0,1,2])
    return computer

def main_logic(computer,user):
    if (computer == 0 and user == 1):
        print("Computer Wins")
    
    elif (computer == 0 and user == 2):
        print("User Wins")

    elif (computer == 0 and user == 0):
        print("Tie")

    elif (computer == 1 and user == 0):
        print("User Wins")

    elif (computer == 1 and user == 2):
        print("Computer Wins")

    elif (computer == 1 and user == 1):
        print("Tie")
    
    elif (computer == 2 and user == 0):
        print("Computer Wins")

    elif (computer == 2 and user == 1):
        print("User Wins")

    elif (computer == 2 and user == 2):
        print("Tie")
    
    else:
        print("Something Went Wrong") 

dict = {"s":0, "w":1, "g":2}
rev_dict = {0: "snake", 1: "water", 2: "gun"}
user = dict[user_input()]
computer = computer_input()
print(f"Computer selected {rev_dict[computer]}")
main_logic(computer, user)
