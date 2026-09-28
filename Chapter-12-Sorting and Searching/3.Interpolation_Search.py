'''
Calculate the probable position of the target value using interpolation formula.
Compare the target value with the element at the calculated position.
If the element matches the target value, return its index.
If the element is less than the target value, search in the right half of the list.
If the element is greater than the target value, search in the left half of the list.
Repeat steps 1-5 until the target value is found or the search interval is empty.'''



my_list = [1,2,3,4,5,6,7,8,9]
target_value = int(input("Enter a number between 0 to 9:\t"))
def binary_search(arr,tar,low,high):
    while low <= high: 
        i = low + ((high - low) // (arr[high] - arr[low])) * (tar - arr[low])
        if arr[i] == tar:
            return i
        elif arr[i] > tar:
            high = i - 1
        elif arr[i] < tar:
            low = i + 1    
        else:
            return -1
            
index_position = binary_search(my_list,target_value, 0, len(my_list)-1)
if index_position != -1:
    print(f"Target value {target_value} is found at index-{index_position}")
else:
    print(f"Target value {target_value} not found")