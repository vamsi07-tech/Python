'''Write a python program to rename a file to renamed_by_ python.txt. '''

with open("F:\\Python\\Chapter-9 - File I_O\\log.txt") as f:
    txt = f.read()

with open("F:\\Python\\Chapter-9 - File I_O\\renamed_by_ python.txt","w") as f1:
    f1.write(txt)