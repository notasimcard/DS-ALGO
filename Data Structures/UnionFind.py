"""
Union Find / Disjoint Set
- To begin using Union Find, first construct bijection (For array based union find)
    - Bijection: Mapping between your object and the integers in the range [0, n) where n = length of your input
- At first, every value is a root node
- Path compression is what give Union Find amortized constant time α(n)
- Path compression happens during a find operation AND union operations
- We lazily do path compression, so It only applies to the nodes which we unify.
""" 
#TODO: Implement using dictionary[key = element, value = position], root_list = [list of roots corressponding to  key's position] nd component_size list



from collections import defaultdict

class UnionFind:
    def __init__(self, size: int):
        if size <= 0:
            return Exception("Size <= 0 not allowed")
        # Number of elements in Union Find
        self.size = size
            # Root Id of each element
            # Initially everyone is their own root
        self.root_ids = []
        # Stores value of each component size, Initally all 1
        self.comp_size = []
        # Number of components, 
        self.comp_number = size
        for i in range(size):
            self.root_id.append(i)
            self.comp_size.append(1)
    

    def find(self, n: int):
        """
            Find which component element 'n' belongs to, takes amortized time.
        """
        # root of the component, initially assume it's intself
        root = n
        while root != self.root_ids[root]:
            root = self.root_ids[root]

        # Path Compressing, so that every element we touched will have its root directly point to root as parent
        # Power that gives amortized time complexity
        while n != root:
            # Question to always ask yourself,
            #   1. What am I updating next ?
            #   2. What am I updating now ?
            #   3. Do I need to store the old value or new value or index that I updated just now
            next = self.root_ids[n]
            self.root_ids[n] = root
            n = next
        
        return root


    def are_connected(self, p: int, q: int) -> bool:
        # Find if two elements are connected
        # Conected elements have same root
        return self.find(p) == self.find(q)


    def get_component_size(self, p: int):
        # Get the size of the component, q belongs to.
        return self.comp_size[self.find(p)] 


    def size(self):
        # Return the number of elelements in the UnionFind / Disjoint set 
        return self.size


    def components(self):
        return self.comp_number


    def union(self, p: int, q: int):
        if self.are_connected(p, q):
            return

        p_root = self.find(p)
        q_root = self.find(q)

        if self.comp_size[p_root] >= self.comp_size[q_root]:
            self.comp_size[p_root] += self.components[q_root]
            self.root_ids[q_root] = p_root
        else:
            self.comp_size[q_root] += self.comp_size[p_root]
            self.root_ids[p_root] = q_root

        self.comp_number -= 1
