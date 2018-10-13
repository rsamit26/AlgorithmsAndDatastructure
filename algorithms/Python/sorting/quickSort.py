"""
Algorithm for sorting using quick sort
"""


def partition(arr, l, r):
    x = arr[l]
    i = l

    for j in range(l + 1, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[l] = arr[l], arr[i]
    return i


def quick_sort(arr, l, r):
    if l < r:
        q = partition(arr, l, r)

        quick_sort(arr, l, q)
        quick_sort(arr, q + 1, r)


arr = [12, 11, 13, 5, 6, 7]
quick_sort(arr, 0, len(arr))
print(arr)
