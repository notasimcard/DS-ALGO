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

#TODO: Min heap to Max heap and vice versa
#TODO: Binary heap implementation using array
#TODO: Add elements to PQ
#TODO: Remove elements from binary heap 1. Polling 2. Removing non root element
#TODO: Multiple nodes with same value (Store multiple position for the same key)

class KeyValue:
    def __init__(self, key, value):
        if key is None or type(key) != int or type(key) != str or type(key) != tuple:
            raise Exception("Unhashable key!")
        self.key, self.value = key, value


class HashTable:
    def __init__(self, capacity=None):
        if capacity is None or capacity < 16:
            self.capacity = 16
        else:
            self.capacity = capacity
        self.hash_table = [[] for _ in range(self.capacity)]
        self.current_threshold = 0
        self.load_factor = 0.75
        self.max_threshold = self.load_factor * self.capacity


    def add(self, key, value):
        key_value = KeyValue(key, value)
        hash = self._hash(key)
        self.hash_table[hash].append(key_value)

    def _hash(self, key):
        if type(key) == int:
            return abs(key)
        else:
            hash = 0
            for character in key:
                hash += ord(character)
        return hash % self.capacity


class PQ_heap:
    def __init__(self):
        self.heap = []
