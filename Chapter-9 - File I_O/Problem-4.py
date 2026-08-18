'''A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.  '''

with open("F:\\Python\\Chapter-9 - File I_O\\file.txt") as f:
    txt = f.read()

newtxt = txt.replace("Donkey","####")    

with open("F:\\Python\\Chapter-9 - File I_O\\file.txt","w") as f:
    txt = f.write(newtxt)