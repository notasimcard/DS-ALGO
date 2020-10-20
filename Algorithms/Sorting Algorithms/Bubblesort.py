"""
Bubble Sort
- Time complexity: O(n^2)
- Space complexity: O(1)
- Stable Search algorithm
"""

def  bubblesort(arr):
    # boolean to check if we need to sort
    needs_sorting = True
    while needs_sorting:
        needs_sorting = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                needs_sorting = True

arr = [2, 7, 4, 1, 5, 3]
bubblesort(arr)
print(arr)