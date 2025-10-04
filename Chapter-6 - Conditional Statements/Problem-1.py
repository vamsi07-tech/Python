numbers = []
a = int(input("Enter a number: "))
numbers.append(a)
a = int(input("Enter a number: "))
numbers.append(a)
a = int(input("Enter a number: "))
numbers.append(a)
a = int(input("Enter a number: "))
numbers.append(a)

print("List:", numbers)

if numbers[0] > numbers[1] and numbers[0] > numbers[2] and numbers[0] > numbers[3]:
    print("Greatest number is:", numbers[0])
elif numbers[1] > numbers[0] and numbers[1] > numbers[2] and numbers[1] > numbers[3]:
    print("Greatest number is:", numbers[1])
elif numbers[2] > numbers[0] and numbers[2] > numbers[1] and numbers[2] > numbers[3]:
    print("Greatest number is:", numbers[2])
elif numbers[3] > numbers[0] and numbers[3] > numbers[1] and numbers[3] > numbers[2]:
    print("Greatest number is:", numbers[3])
