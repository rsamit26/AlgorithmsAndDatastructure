"""
ith Smallest element in an array

worst case time :: O(n)
"""


def find_median(a):
    n = len(a)
    a.sort()
    # check for even case
    if n % 2 != 0:
        return float(a[n // 2])

    return float((a[int((n - 1) // 2)] +
                  a[int(n / 2)]) // 2.0)


def ith_smallest_ele(arr, i):
    n = len(arr)
    i = 0
    m = []
    while i < n:
        p = arr[i:i+5]
        p.sort(reverse=True)
        arr[i:i+5] = p
        i += 5

    print(arr)


arr = [1, 3, 4, 2, 7, 5, 8, 6, 11, 45, 97, 12, 55, 40]
ith_smallest_ele(arr, 5)

# arr = [ 1, 3, 4, 2, 7, 5, 8, 6, 11,45,97,12,55,40 ]
# arr.sort(reverse=True)
# print(arr)
