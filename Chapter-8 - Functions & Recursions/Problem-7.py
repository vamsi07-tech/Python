'''Write a python function to print multiplication table of a given number '''

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Enter a number to print its multiplication table: "))
multiplication_table(num)


