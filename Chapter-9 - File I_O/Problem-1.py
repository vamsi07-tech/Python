'''Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. '''

with open("F:\\Python\\Chapter-9 - File I_O\\Poem.txt") as f:
    str = f.read()

if ("twinkle" in str ):
    print("twinkle is available")

count = str.lower().count("twinkle")
print(f"twinkle comes {count} times")