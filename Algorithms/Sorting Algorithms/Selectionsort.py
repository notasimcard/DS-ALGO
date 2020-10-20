"""
Selection Sort
- Most intuitive sorting
- Time complexity: O(n^2)
- Space Complexity: O(1) for in place, O(n) for not in place
- 
"""

def selectionsort(arr):
    if arr is None or len(arr) == 0:
        return

    for i in range(len(arr)-1):
        # Minimum value index
        i_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i_min]:
                # Update index of minimum element
                i_min = j
        arr[i], arr[i_min] = arr[i_min], arr[i]


arr = [2, 7, 4, 1, 5, 3]
selectionsort(arr)
print(arr)