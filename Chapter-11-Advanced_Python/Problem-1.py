'''Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not
present, a message without exiting the program must be printed prompting the same.'''

try:
    with open("F:\\Python\\Chapter-11-Advanced_Python.py\\txt1.txt") as f1:
       content1 =f1.read()
    with open("F:\\Python\\Chapter-11-Advanced_Python.py\\txt2.txt") as f2:
        content2 =f2.read()
    with open("F:\\Python\\Chapter-11-Advanced_Python.py\\txt3.txt") as f3:
        content3 =f3.read()
except FileNotFoundError:
    print("File not found!")
else:
   print("File read successfully.")