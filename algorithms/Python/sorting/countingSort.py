"""
Linear time sorting :: counting sort algorithm
array = (1.....n) where n>0
"""


def counting_sort(arr):
    c = [0]*(max(arr)+1)
    b = [0]*len(arr)
    for i in arr:
        c[i] += 1
    for j in range(2, len(c)):
        c[j] += c[j-1]
    for k in range(len(arr)):
        b[c[arr[k]]-1] = arr[k]
        c[arr[k]] -= 1
    return b

print(counting_sort([4, 1,9, 55, 3,1861,24499, 4, 3]))