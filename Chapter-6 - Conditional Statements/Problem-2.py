marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (marks1 + marks2 + marks3)/300

if(total_percentage>=40):
    print("You are pass")

else:
    print("You failed, try again next year!")
