def my_function(a, b,*args, c=10,**kwargs):
   print(f"a: {a}")
   print(f"args: {args}")
   print(f"c: {c}")
   print(f"kwargs: {kwargs}")
   print(f"b: {b}")

my_function(1,2,3,4,5, c=20, name="Bob", country="USA")
my_function(1,2)