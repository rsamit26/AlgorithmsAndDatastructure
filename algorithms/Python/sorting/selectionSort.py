"""
Algorithm for selection sort
"""

def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i

        for j in range(i+1, len(arr)):

            if arr[min_index] > arr[j]:

                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


print(selection_sort([4,2,6,7,8,12,5,8,19]))

