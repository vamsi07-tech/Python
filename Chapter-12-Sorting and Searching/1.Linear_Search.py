'''
Start from the first element of the list.
Compare each element of the list with the target value.
If the element matches the target value, return its index.
If the target value is not found after iterating through the entire list, return -1.'''

my_list = [5,6,8,4,0,3,2,1,9]
target_value = int(input("Enter a number between 0 to 9:\t"))

def linear_search(arr,tar):
    for i in range(len(arr)):
        if arr[i] == target_value:
           return i      
    return -1       

index_position = linear_search(my_list, target_value)
if index_position != -1:
    print(f"Target value {target_value} is found at index-{index_position}")
else:
    print(f"Target value {target_value} not found")