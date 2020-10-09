"""
Priority Queue:
    1. Implementation (heaps, unordered list)
    2. Convert Min PQ --> Max PQ
    3. Adding Element to PQ ( O(log(n)) )
        - Add new element to the new position
        - Bubble up the new element (Compare with parent element to keep the heap invariant)
    4. Removing Elements from PQ ( Polling = O(log(n)), Remove(i) = O(n) || O(log(n) using Hashtable)
        - Swap del_element with last element
        - Remove del_element
        - Bubble up / down the former last element depending upon the position and maintain heap invariant
"""

# Heap implementation using Binary Tree
# Binary Heap (Min Heap)
# left child  = 2i+1, right child = 2i+2
# left child  = 2i, right child = 2i+1, if we use dummy value for 0th index
# parent = [(i-1) / 2 for left, (i-2) / 2 for right] or n // 2 if we put 0 as our dummy value in our initial list
from os import removedirs


class BinHeap:
    def __init__(self, eterable=None):
        # Using list to build complete binary tree.
        if eterable:
            self.heap = [0] + eterable
            self.heap_size = len(eterable)
        else:
            self.heap = [0]
            self.heap_size = 0


    def insert(self, elem):
        # Add new element to the last index
        self.heap.append(elem)
        self.heap_size += 1
        # Bubble up to maintain heap invariant
        self.bubble_up(self.heap_size)


    # Removing most priority element which is the root.
    def poll(self):
        # 0th index has our dummy value 0. So ignoring 0th index element
        min_root = self.heap[1]
        self.heap[1], self.heap[self.heap_size] = self.heap[self.heap_size], self.heap[1]
        self.heap.pop()
        self.heap_size -= 1
        self.bubble_down(1)
        return min_root


    def remove(self, del_value):
        # TODO: Use Hash table
        # O(1) time, hash table, adds significant amount of overhead
        # Useful if you frequently remove random elements

        # O(n) time, no hash table, no map overhead
        # Useful if you don't remove random element often
        if del_value is None:
            return

        removed_element = None
        del_index = None
        for i, _ in enumerate(self.heap):
            if self.heap[i] == del_value:
                self.heap[i], self.heap[self.heap_size] = self.heap[self.heap_size], self.heap[i]
                removed_element = self.heap.pop()
                self.heap_size -= 1
                # parent is greater, do bubble up
                if self.heap[i // 2] > self.heap[i]:
                    self.bubble_up(i)     
                else:
                    self.bubble_down(i)
        return removed_element


    def contains(self, seek_elem):
        # TODO: Use Hash table

        # Without Using Hash table, O(n) time
        for element in self.heap:
            if element == seek_elem:
                return True
        return False


    def print_heap(self):
        print(self.heap[1:])


    def bubble_up(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] > self.heap[i]:
                self.heap[i // 2] , self.heap[i] = self.heap[i], self.heap[i // 2]
                i = i // 2
            else:
                return


    def bubble_down(self, i):
        # Check if the heap variant is maintained upto the parent of leaf node
        # We don't care about leaf node, because there is no need to shuffle only the leaf
        while i <= self.heap_size // 2:
            min_child_index = self.min_child(i)
            if self.heap[i] > self.heap[min_child_index]:
                self.heap[i], self.heap[min_child_index] =  self.heap[min_child_index], self.heap[i]
                i = min_child_index
            else:
                return
        return


    def min_child(self, i):
        # Finds the minimum child, return left child if equal
        # Check if the parent has two children
        if (2 * i) + 1 > self.heap_size:
            return 2 * i

        if self.heap[2 * i] <= self.heap[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1


def heapify(array, return_heap=True):
    # Why heapify takes O(n) time instead of O(nlog(n)): http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
    if array is None:
        return array

    i = len(array) // 2
    new_heap = BinHeap(array)

    while i > 0:
        new_heap.bubble_down(i)
        i = i - 1
    
    if return_heap:
        return new_heap
    else:
        return new_heap.heap


def is_min_heap(array, i):
    if i >= len(array):
        return True
    # TODO
    return


def is_max_heap(array, i):
    # TODO
    return


def convert_heaps(array, i):
    # TODO
    return

# Driver Code
heap = BinHeap()
heap.insert(5)
heap.insert(9)
heap.insert(11)
heap.insert(14)
heap.insert(18)
heap.insert(19)
heap.insert(21)
heap.insert(33)
heap.insert(17)
heap.insert(27)
heap.print_heap()
print(f"heap size = {heap.heap_size}")
print("--------------------")
print(f"polled = {heap.poll()}")
heap.print_heap()
print(f"heap size = {heap.heap_size}")
print("--------------------")
print(f"Removed element: {heap.remove(18)}")
heap.print_heap()
print("--------------------")
print(f"Heap contains 13: {heap.contains(13)}")
print(f"Heap contains 33: {heap.contains(33)}")
print("--------------------")
array = [8, 12, 9, 7, 22, 3, 26, 14, 11, 15, 22]
heaped = heapify(array)

if heaped.heap[1:] == [3, 7, 8, 11, 15, 9, 26, 14, 12, 22, 22]:
    print("you just got heaped !!")
else:
    print("Heaping failed")

heaped.print_heap()
print("--------------------")
