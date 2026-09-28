'''
First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
We keep doing this until we get all elements moved to correct position.'''

my_list = [5,7,3,8,2,1,9,4]
print(f"Before Sorting: {my_list}")

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        minpos = i
        for j in range(i,len(my_list)):
          if my_list[j] < my_list[minpos]:
            minpos = j

        x = my_list[i]
        my_list[i] = my_list[minpos]    
        my_list[minpos] = x

selection_sort(my_list)
print(f"After Sorting: {my_list}")