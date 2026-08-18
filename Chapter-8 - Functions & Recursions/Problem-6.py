'''Write a python function which converts inches to cms. '''
def inch_cms(num):
    return (num*2.54)

num = int(input("Enter a number in inches:"))
print(f"{num} inches = {inch_cms(num)}cms")