number = int(input("Enter a Number"))

for i in range(2,number):
    if (number%i)==0:
        print("It is not a Prime Number")
    else:
        print("It is a Prime Number")
        break
