'''
Write a program that asks the user to enter a number and handles:
ValueError if the input is not a number
ZeroDivisionError if you try to divide by zero
Create a custom exception NegativeNumberError and raise it when the user
enters a negative number.'''

# Define custom exception
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    if (num < 0 or num2 < 0):
       raise NegativeNumberError("Error: Negative numbers are not allowed") 
    res = num / num2

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except NegativeNumberError as e:
    print(e)

else:
    print(res)    