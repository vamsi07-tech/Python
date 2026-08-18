'''Write a program to find out whether a file is identical & matches the content of 
another file. '''
with open("F:\\Python\\Chapter-9 - File I_O\\Poem.txt") as f1:
    txt1 = f1.read()
 
with open("F:\\Python\\Chapter-9 - File I_O\\Hiscore.txt") as f2:
    txt2 = f2.read()

if (txt1 == txt2):
    print("Content Matches")
else:
    print("Contenet don't Match")