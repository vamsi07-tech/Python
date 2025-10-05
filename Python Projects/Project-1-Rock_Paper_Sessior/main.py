import random
def rules(computer,user):
    if (computer == user):
        print("Its a Draw")
    else:
        if (computer==0 and user==1):
            print("you win")
        elif (computer==1 and user==0):
            print("you loose")
        elif (computer==0 and user==2):
            print("you loose")
        elif (computer==2 and user==0):
            print("you win")
        elif (computer==2 and user==1):
            print("you loose")
        elif (computer==1 and user==2):
            print("you win")
        else:
            print("Something went wrong")


def user_input():
    var_dic = {'R':0, "P":1, "S":2}
    rev_dic = {0:'Rock', 1:'Paper', 2:'Scissor'}
    i=0
    while i<3:
        choice = (input("Enter your Choice: ")).upper()
        if (choice not in var_dic):
            print("Invalid Input")
            i=i+1
        else:
            user =int(var_dic[choice])
            print(f"You Selected {rev_dic[user]}")
            return user
    print("Too many invalid attempts. You lose!")


def welcome():
    print("Welcome to Rock, Paper, Scissor Game:")
    print("-------------------------------------")
    print("Select \t Rock \t Paper \t or Scissor")

def computer_input():
    computer = random.choice([0, 1, 2])
    rev_dic = {0:'Rock', 1:'Paper', 2:'Scissor'}
    print(f"Computer Selected {rev_dic[int(computer)]}")
    return int(computer)


welcome()
user = user_input()
if user is not None:
    computer = computer_input()
    rules(computer,user)
