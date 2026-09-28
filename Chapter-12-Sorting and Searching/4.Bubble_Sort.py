'''
Bubble Sort algorithm, sorts an array by repeatedly comparing adjacent elements and swapping them if they are in the wrong order.
The algorithm iterates through the array multiple times, with each pass pushing the largest unsorted element to its correct position at the end.
Code includes an optimization: if no swaps are made during a pass, the array is already sorted, and the sorting process stops.
'''

my_list = [5,7,3,8,2,1,9,4]
print(f"Before Sorting: {my_list}")

def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        #print(f"i={i}")
        for j in range(i):
          if my_list[j] > my_list[j+1]:
            x = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = x

bubble_sort(my_list)
print(f"After Sorting: {my_list}")