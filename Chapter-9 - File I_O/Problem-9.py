'''Write a program to make a copy of a text file  '''

with open("F:\\Python\\Chapter-9 - File I_O\\log.txt") as f:
    txt = f.read()

with open("F:\\Python\\Chapter-9 - File I_O\\this.txt","w") as f1:
    f1.write(txt)