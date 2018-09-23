"""
ith smallest element of array
divide and conquer algorithm

## Worst Case O(n^2)

"""


def rand_partition(arr, low, r):
    x = arr[r]
    i = low

    for j in range(low, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def ith_smallest(arr, low, r, i):
    if i > len(arr):
        return "Index is greater than no of element in array"
    if low == r:
        return arr[low]
    t = rand_partition(arr, low, r)

    k = t - low + 1

    if i == k:
        return arr[t]
    elif i < k:
        return ith_smallest(arr, low, t - 1, i)
    else:
        return ith_smallest(arr, t + 1, r, i - k)


ar = [-4, 34, 0, 12, 11, 13, 5, 6, 7]

print(ith_smallest(ar, 0, len(ar) - 1, 1))
