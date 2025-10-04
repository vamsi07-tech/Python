s = {8, 7, 12, "Harry", [1,2]} 

'''No, you cannot include a list inside a set in Python because lists are mutable and unhashable.
If you try to run this code:

s={8,7,12,"Harry",[1,2]}
You will get a TypeError: unhashable type: 'list'.'''