"""
Insertion Sort
- Time complexity: O(n)
- Space complexity: O(1)
"""

def insertionsort(arr):
    if arr is None or len(arr) == 0:
        return

    for i in range(1, len(arr)):
        value = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > value:
            arr[hole] = arr[hole-1]
            hole = hole - 1
        arr[hole] = value


arr = [2, 7, 4, 1, 5, 3]
insertionsort(arr)
print(arr)