"""
Radix sort algorithm -> least significant digit
"""


def radix_sort_util(arr, ex):
    n = len(arr)
    c = [0] * 10
    b = [0] * n
    for i in range(0, n):
        ind = arr[i] // ex
        c[ind % 10] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    for j in range(n - 1, -1, -1):
        ind = arr[j] // ex
        b[c[ind % 10] - 1] = arr[j]
        c[ind % 10] -= 1
    for i in range(0, len(arr)):
        arr[i] = b[i]



def radix_sort(arr):
    mx = max(arr)
    ex = 1

    while mx / ex > 0:
        radix_sort_util(arr, ex)
        ex *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]

radix_sort(arr)
print(arr)
