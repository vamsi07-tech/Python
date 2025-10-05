'''
* * * 
*   *    
* * *
'''
number = int(input("Enter a Number"))

for i in range(1,number+1):
    if(i==1 or i==number):
        print("*"*number) 
    else:
        print("*",end="")
        print(" "*(number-2),end="")
        print("*")
