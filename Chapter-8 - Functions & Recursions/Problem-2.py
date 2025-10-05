'''
F = (C x 1.8) +32
'''
def farh(c):
    F = (c * 1.8) +32
    print(f"Temperature in Fahrenheit is {F}")

c=int(input("Enter a temperature in celsius"))
farh(c)