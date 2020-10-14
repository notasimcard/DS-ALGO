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
#TODO: Heap construction using heapify


class ValueNode:
    def __init__(self, value, value_index):
        if value is None or (type(value) != int and type(value) != str):
            raise Exception("Can only take integers or string.")
        self.value, self.value_index = value, value_index


class HashTable:
    def __init__(self, capacity=None):
        if capacity is None or capacity < 16:
            self.capacity = 16
        else:
            self.capacity = capacity
        self.hash_table = [[] for _ in range(self.capacity)]
        self.current_threshold = 0
        self.load_factor = 0.75
        self.max_threshold = int(self.load_factor * self.capacity)


    def insert(self, value, value_index):
        # value = input, value_index = index in Priority Q
        # Can handle both +ve and -ve value
        value_info = ValueNode(value, value_index)
        hash = self._hash(value)
        self.hash_table[hash].append(value_info)
        self.current_threshold += 1
        if self.current_threshold == self.max_threshold:
            self._resize()


    def contains(self, value):
        hash = self._hash(value)
        for value_node in self.hash_table[hash]:
            if value_node.value == value:
                return value_node.value_index
        return None


    def remove(self, del_value):
        hash = self._hash(del_value)
        for index, value_node in enumerate(self.hash_table[hash]):
            if value_node.value == del_value:
                return self.hash_table[hash].pop(index)


    def update(self, value, old_index, new_index):
        hash = self._hash(value)
        for value_node in self.hash_table[hash]:
            if value_node.value == value and value_node.value_index == old_index:
                value_node.value_index = new_index
                return


    def _hash(self, key):
        hash = 0
        if type(key) == int:
            hash = abs(key)
        else:
            for character in key:
                hash += ord(character)
        return hash % self.capacity


    def _resize(self):
        self.capacity = 2 * self.capacity
        self.current_threshold = 0
        self.max_threshold = int(self.load_factor * self.capacity)

        old_hash_table = self.hash_table
        self.hash_table =  [[] for _ in range(self.capacity)]
        for bucket in old_hash_table:
            for value_node in bucket:
                self.insert(value_node)


    def print_table(self):
        print("{:^10}{:^10}{:^10}".format("Map Index", "Value", "Heap Index"))
        for index, bucket in enumerate(self.hash_table):
            if len(bucket) > 0:
                for value_node in bucket:
                    print("{:^10}{:^10}{:^10}".format(index, value_node.value, value_node.value_index))


class PQ:
    """
        Priority Queue implementation using binary heap.
        Heap is a tree structure, which has to maintain heap variant.
        Heap variant:
            Parent Node should be greater than child Node (Max Heap)
            Parent Node should be smaller than child Node (Min Heap)
        Priority Queue is an abstract data type, so heap is not the only way to implent Priority Queue
        This is Min Heap Implementation.
        For Binary tree strucutre:
            odd index = left child, even index= right child
            i = current index
            left_child = 2i + 1, right child = 2i + 2
            left_child_parent = i - 1 / 2, right_child _parent = i - 2 / 2
    """
    def __init__(self):
        self.heap = []
        self.value_map = HashTable()


    def insert(self, value):
        # Takes O(log(n))
        # Add new value at the tail
        self.heap.append(value)
        # Add value entry to hash table
        self.value_map.insert(value, len(self.heap) - 1)
        self._bubble_up(len(self.heap) - 1)


    def heapify(self, values):
        # Using heapify to build a Prioirty queue from a list
        # Time complexity will be O(n)
        # Ignoring all leaf nodes, as leaf nodes are already 
        self.heap = values
        start = (len(values) - 1) // 2
        while start >= 0 :
            self._heapify_bubble_down(start)
            start -= 1

    def peek(self):
        return self.heap[0]


    def poll(self):
        # Takes O(log(n))
        return self.remove(self.heap[0])


    def remove(self, del_value):
        # Takes O(log(n)) using hash map, otherwise O(n)
        # Find the del_value's first index = i
        # Switch it with the last value
        # Delete last value

        # Returns the first index of the value
        # If 5 is present at position 8 and 10 8 will be returned
        curr_index = self.value_map.contains(del_value)
        if curr_index is None:
            return None

        if curr_index == len(self.heap) - 1:
            # remove the last value
            self.heap.pop()
            # remove the first del_value present in the hash map
            self.value_map.remove(del_value)
            return

        # Update hash table
        self.value_map.update(self.heap[len(self.heap)-1], len(self.heap)-1, curr_index)
        # swap the del_value with the last value in the queue
        self.heap[curr_index], self.heap[-1] = self.heap[-1], self.heap[curr_index]
        # remove the last value
        self.heap.pop()

        # remove the first del_value present in the hash map
        self.value_map.remove(del_value)

        # Maintain the heap invariant
        # case 1: Parent > Children, Bubble up from i
        # case 2: Parent < Children, Bubble down from i
        # case 3: heap invariant is maintained
        self._bubble_up(curr_index)
        self._bubble_down(curr_index)


        
    def contains(self, search_value):
        # Searches for the value, and returns first index it hits
        # There can be same values at multiple heap position
        return self.value_map.contains(search_value)


    def _bubble_up(self, index):
        # switch child with parent if  child < parent for Min Heap until Heap Invariant is maintained
        while index > 0:
            # odd index == left child, even index == right child
            if index % 2 == 1:
                parent_index = (index - 1) // 2
            else:
                parent_index = (index - 2) // 2

            if self.heap[parent_index] > self.heap[index]:
                # Update the hash table for values at both indices
                self.value_map.update(self.heap[parent_index], parent_index, index)
                self.value_map.update(self.heap[index], index, parent_index)
                # Switch parent <--> Child value
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                # Move up and check parent
                index = parent_index
            else:
                return


    def _bubble_down(self, index):
        # Switch Parent with min(left_child, right_child) until heap invariant is maintained
        while True:            
            lc_index = (index * 2) + 1
            rc_index = (index * 2) + 1

            # Case 1: Is a leaf node
            if lc_index >= len(self.heap):
                return

            #Case 2: Only left child is present
            # Assume left is the minium child
            mc_index = lc_index

            # Case 3: Both children are present
            if rc_index < len(self.heap) and  min(self.heap[lc_index], self.heap[rc_index]) == self.heap[rc_index]:
                mc_index = rc_index

            # Swap the parent and minimum child if parent > children, end otherwise
            if self.heap[index] > self.heap[mc_index]:
                # Update the hash table for values at both indices
                self.value_map.update(self.heap[mc_index], mc_index, index)
                self.value_map.update(self.heap[index], index, mc_index)
                # Update heap
                self.heap[index], self.heap[mc_index] = self.heap[mc_index], self.heap[index]
                index = mc_index
            else:
                return


    def _heapify_bubble_down(self, index):
        #TODO: Heapify
        return


    def print_heap(self):
        print(self.heap)


    def print_map(self):
        self.value_map.print_table()

pq = PQ()
pq.insert(35)
pq.insert(33)
pq.insert(42)
pq.insert(10)
pq.insert(14)
pq.insert(19)
pq.insert(27)
pq.insert(44)
pq.insert(26)
pq.insert(31)

print("Insert:\n")
pq.print_heap()
print("---------------------------------------")
pq.print_map()
print("---------------------------------------")


print("Remove:\n")
pq.remove(10)
pq.print_heap()
print("---------------------------------------")
pq.print_map()
print("---------------------------------------")