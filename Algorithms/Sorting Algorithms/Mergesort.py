"""
Merge Sort
- Time complexity: O(nlog(n))
- Space comlexity: O(n)
- Stable
"""

def mergesort(arr):
    # Base case
    if len(arr) < 2:
        return

    mid = len(arr) // 2
    left = arr[0: mid]
    right = arr[mid: len(arr)]
    mergesort(left)
    mergesort(right)
    merge(left, right, arr)


def merge(left, right, arr):
    li = 0
    ri = 0
    ai = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            arr[ai] = left[li]
            li += 1
        else:
            arr[ai] = right[ri]
            ri += 1
        ai += 1
    while li < len(left):
        arr[ai] = left[li]
        li += 1
        ai += 1
    while ri < len(right):
        arr[ai] = right[ri]
        ri += 1
        ai += 1


arr = [2, 7, 4, 1, 5, 3, 10, 6]
mergesort(arr)
print(arr)