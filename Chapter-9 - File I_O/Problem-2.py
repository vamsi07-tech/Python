'''The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score. '''

import random
def game():
    with open("F:\\Python\\Chapter-9 - File I_O\\Hiscore.txt") as f:
        Hiscore = int(f.read())
        if (Hiscore == ""):
            Hiscore = 0
        else:
            Hiscore = Hiscore

    score = random.randint(1,100)
    print(f"score is {score}") 
    if (score > Hiscore):
        f = open("F:\\Python\\Chapter-9 - File I_O\\Hiscore.txt","w")
        f.write(str(score))

    return score

game() 

