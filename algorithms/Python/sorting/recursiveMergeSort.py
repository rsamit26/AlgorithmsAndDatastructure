"""
Merge sort using recursion
"""


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while len(result) < len(right) + len(left):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def req_merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2

    left = req_merge_sort(arr[:mid])
    right = req_merge_sort(arr[mid:])

    return merge(left, right)


ar = [4, 2, 6, 7, 8, 12, 5]
print(req_merge_sort(ar))
