def my_function(**kwargs):
    print(type(kwargs)) 
    for key, value in kwargs.items():
       print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")
my_function()
my_function(a=1, b=2)
