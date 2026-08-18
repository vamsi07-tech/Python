''' Write a program to find the maximum of the numbers in a list using the reduce function.'''
from functools import reduce

number = [2,4,56,34,78,345,234,67,788]

def max(a,b):
    if a > b:
        return a
    return b

max = reduce(max, number)
print(max)