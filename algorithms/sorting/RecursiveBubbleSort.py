"""
Algorithm for bubble sort using recursion

"""


def req_bubble_sort(arr, n):
    if n == 1:  # Base Case when size of array become one or only one element in array
        return arr
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    req_bubble_sort(arr, n - 1)


"""
Testing code for this algorithm
"""
ar = [4, 2, 6, 7, 8, 12, 5, 19]
req_bubble_sort(ar, len(ar))
print(ar)
