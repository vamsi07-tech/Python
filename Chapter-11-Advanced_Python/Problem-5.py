'''Write a program to filter a list of numbers which are divisible by 5.'''
number = [3,5,10,4,23,50,60,100,33,42,66,105]
div_five = list(filter(lambda x: x%5 == 0, number))
print(div_five)