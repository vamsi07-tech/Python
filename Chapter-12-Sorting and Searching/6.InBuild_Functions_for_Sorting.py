my_list = [5,7,3,8,2,1,9,4]
print(f"Before Sorting: {my_list}")
my_list.sort()
print(f"After Sorting Ascending: {my_list}")
my_list.sort(reverse=True)
print(f"After Sorting Descending: {my_list}")

my_list = [5,7,3,2,4]
print(f"Before Sorting: {my_list}")
print(f"After Sorting: {sorted(my_list)}")