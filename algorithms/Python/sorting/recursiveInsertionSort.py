"""
Algorithm for insertion sort using recursion

"""

def req_insertion_sort(arr, n):

    if n <= 1:
        return
    print("Recursion Start")
    req_insertion_sort(arr, n - 1)
    print(arr, n)
    print("Recursion End")
    last = arr[n - 1]
    print("last", last)

    j = n - 2
    print("value of j", j)

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last

arr = [4,2,6,7,8,12,5,19]
req_insertion_sort(arr, len(arr))
print(arr)