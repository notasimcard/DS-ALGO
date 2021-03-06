"""
Quicksort Implementation
- Most language uses quicksort for its sorting
- Time complexity: Average case: O(nlog(n)), Worst case: O(n^2)
- Space Complexity: Average case: O(log(n)), Worst case: O(n)
- Quicksort calls itself on the order of log(n) times 
    (in the average case, worst case number of calls is O(n)), 
    at each recursive call a new stack frame of constant size must be allocated. 
    Hence the O(log(n)) space complexity.
- We can have O(nlog(n)) with high probability if we use randomized version
    of quicksort
- Not stable, https://www.geeksforgeeks.org/stability-in-sorting-algorithms/
"""

def quicksort(arr, start, end):
    # Base condition
    # Segment might not be invalid
    # Segment only has one element
    if start >= end:
        return
    p_index = partition(arr, start, end)
    quicksort(arr, start, p_index-1)
    quicksort(arr, p_index+1, end)


def partition(arr, start, end):
    # Returns index of rearranged element, pivot    
    pivot = arr[end]
    # initially set p_index to 0
    p_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1
    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index


# Driver Code
arr = [7, 2, 1, 6, 8, 5, 3, 4]
quicksort(arr, 0, len(arr)-1)
print(arr)