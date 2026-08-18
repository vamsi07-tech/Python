'''Write a program using functions to find greatest of three numbers.'''
def great(a,b,c):
    if (a>b and a>c):
        print(f"{a} is the greatest")
    elif (b>a and b>c):
        print(f"{b} is the greatest")
    else:
        print(f"{c} is the greatest")

a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
great(a,b,c)