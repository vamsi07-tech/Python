'''Write a function 
print_details(**kwargs) that prints key-value pairs passed
as arguments, for example:
   print_details(name="Alice", age=25, city="Delhi")
# Output:
# name: Alice
# age: 25
# city: Delhi'''

def print_details(**kwargs):
    """Print key-value pairs passed as keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Test the function
print_details(name="Alice", age=25, city="Delhi")
print()
print_details(product="Laptop", price=50000, brand="Dell")
print()
print_details(name="Bob", occupation="Engineer", salary=80000, location="Mumbai")