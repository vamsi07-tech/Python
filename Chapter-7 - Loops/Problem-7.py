'''
  * 
 *** 
*****
'''

number = int(input("Enter a Number"))

for i in range(1,number+1):
    print(" "*(number-i),end="") 
    print("*"*(2*i-1))
