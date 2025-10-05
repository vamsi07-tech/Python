'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

number = int(input("Enter a Number"))
for i in range(1,(2*number-1)):
    if (i<=number):
        print(" "*(number-i),end="")
        print("*"*(2*i-1))
    else:
        print(" "*(i-number),end="")
        print("*"*(2*(2*number-i)-1))