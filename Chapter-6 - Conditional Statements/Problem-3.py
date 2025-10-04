comment=input("Enter your comment: ")
P1= "Make a lot of money"
P2= "buy now" 
P3= "subscribe this" 
P4= "click this"
if (P1 in comment or P2 in comment or P3 in comment or P4 in comment):
    print("Spam Message")
else:
    print("Not a Spam Messsage")
