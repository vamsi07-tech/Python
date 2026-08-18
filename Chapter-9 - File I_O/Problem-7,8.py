'''Write a program to mine a log file and find out whether it contains ‘python’. 
Write a program to find out the line number where python is present from ques 6. '''

with open("F:\\Python\\Chapter-9 - File I_O\\log.txt") as f:
    txt = f.readlines()

count = 0

for i in txt:
    if ("Python" in i):
        count += 1
        print(f"python avaialble in line {count}")
        
else:
    print("python not available")

