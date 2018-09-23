"""
Insertion sort algorithm
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Testing code

ar = [5, 6, 2, 1, 7, 88, 55, 61, 7]
print(insertion_sort(ar))
