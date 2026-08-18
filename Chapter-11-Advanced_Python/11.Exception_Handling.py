def check_age(age):
    if age <18:
       raise ValueError("Age must be 18 or older!")
    return"Access granted."
try:
    print(check_age(20)) # Access granted.
    print(check_age(16)) # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")


try:
    file=open("test.txt","r")
    content =file.read()
except FileNotFoundError:
    print("File not found!")
else:
   print("File read successfully.")
   print(f"File contents:\n{content}")
finally:
   file.close()  
