"""
Algorithm for bubble sort
"""

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                continue

    return arr


print(bubble_sort([4,2,6,7,8,12,5,19]))