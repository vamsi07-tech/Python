'''
factorial(1)=1
factorial(2)=2x1
factorial(3)=3x2x1
factorial(4)=4x3x2x1
factorial(5)=5x4x3x2x1
factorial(n)=nx(n-1)x....x2x1
factorial(n)=nxfactorial(n-1)
'''
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

n=int(input("Enter a number"))
print(f"The factorial of {n} is {fact(n)}")