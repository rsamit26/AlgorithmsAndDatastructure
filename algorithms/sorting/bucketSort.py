"""
Bucket sort algorithm ::

"""
import math


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def hashing(arr):
    m = max(arr)
    result = [m, int(math.sqrt(len(arr)))]
    return result


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


def bucketSort(array):
    code = hashing(array)
    buckets = [list() for _ in range(code[1])]
    for i in array:
        x = re_hashing(i, code)
        buck = buckets[x]
        buck.append(i)
    for bucket in buckets:
        insertion_sort(bucket)

    ndx = 0
    for b in range(len(buckets)):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1


"""
Test code
"""

ar = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68]
# ar = [6, 8, 1, 45, 12]
bucketSort(ar)

print(ar)

# result :: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
