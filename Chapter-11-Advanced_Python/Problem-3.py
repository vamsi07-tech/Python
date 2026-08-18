'''Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionErrorʼ .'''

try:
    a = int(input("Enter 1st number:\n"))
    b = int(input("Enter 2nd number:\n"))
    print(a/b)

except ZeroDivisionError:
    print("Infinite")

