'''Store the multiplication tables generated in problem 2 in a file named Tables.txt .
'''
num = int(input("Enter a number"))
table = []

table = [num * i for i in range(1, 11)]
print(table)

with open ("F:\\Python\\Chapter-11-Advanced_Python.\\Tables.txt", "a") as f:
    f.write(str(table))