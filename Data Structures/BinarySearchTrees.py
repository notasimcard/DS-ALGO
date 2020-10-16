"""
Uses:
    1. Map and Abstract Data Type(ADT)s implementation
    2. Red Black Trees
    3. AVL Trees
    4. Splay Trees
    5. Syntax Trees
    6. Treap
    7. Binary heaps, etc
"""
#TODO: Binary Insertion
#TODO: Binary Removal
    # Case 1: Node to remove is a leaf node
    # Case 2: Node to remove has only left subtree
    # Case 3: Node to remove has only right subtree
    # Case 4: Node to remove has both subtrees
        # I) Successor can be the largest value in the left subtree
        # II) or, Successor can be the smallest value in the right subtree
#TODO Tree Traversals:
    # Preorder
    # Inorder : Increasing value order
    # Postorder
    # Level order (BFS)
#TODO: Check if binary search tree is valid or not

class Node:
    # Tree Node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1


class BST:
    # Binary Search Tree class
    def __init__(self):
        self.size = 0
        self.root = None


    def insert(self, insert_value):
        # Create new node
        new_node = Node(insert_value)
        # Increase BST's size
        self.size += 1
        # Current Node in BST
        curr_node = self.root
        # Check if root is present i.e if BST is empty
        # Case I: No root
        if curr_node is None:
            self.root = new_node
            return

        # We return after we finish inserting
        while True:
            # Case II: Insert value < node value, current_node = left node
            if insert_value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return
                curr_node = curr_node.left
            # Case III: Insert value > node_value, current_node = right node
            elif insert_value > curr_node.value:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return
                curr_node = curr_node.right
            # Case IV: Insert value == current_node.value, increase count
            elif insert_value == curr_node.value:
                curr_node.count += 1
                return

    def traversals(self, traverse="in_order"):
        if traverse == "in_order":
            return self.in_order(self.root)
        elif traverse == "pre_order":
            return self.pre_order(self.root)
        elif traverse == "post_order":
            return self.post_order(self.root)
        elif traverse == "level_order":
            return self.level_order(self.root)
        else:
            return None


    def in_order(self, node, res=[]):
        # left -> root -> right
        if node:
            res = self.in_order(node.left , res)
            res.append(f"{str(node.value)}({str(node.count)})")
            res = self.in_order(node.right, res)
        return res


    def pre_order(self, node, res=[]):
        # root -> left -> right
        if node:
            res.append(f"{str(node.value)}({str(node.count)})")
            res = self.pre_order(node.left)
            res = self.pre_order(node.right)
        return res


    def post_order(self, node, res=[]):
        # left -> right -> root
        if node:
            res = self.post_order(node.left, res)
            res = self.post_order(node.right, res)
            res.append(f"{str(node.value)}({str(node.count)})")
        return res


    def level_order(self):
        # level 1 --> level 2 --> level n
        if self.root is None:
            return None
        curr_level_nodes = [self.root]
        queue = []
        while True:
            next_level_nodes = []
            for node in curr_level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            queue.append(curr_level_nodes)

            if len(next_level_nodes) == 0:
                return queue

            curr_level_nodes = next_level_nodes

    def __str__(self):
        return ' - '.join(self.traversals())


# Driver code
bst = BST()
bst.insert(10)
bst.insert(23)
bst.insert(11)
bst.insert(1)
bst.insert(6)
bst.insert(19)
bst.insert(3)
bst.insert(10)
bst.insert(23)
bst.insert(11)
bst.insert(11)
bst.insert(16)
bst.insert(119)
bst.insert(13)

print("In Order")
print(bst)
print("-----------------------")
print("Pre Order")
print(' - '.join(bst.pre_order(bst.root)))
print("-----------------------")
print("Post Order")
print(' - '.join(bst.post_order(bst.root)))
print("-----------------------")
print("Level Order")
for level_nodes in bst.level_order():
    for node in level_nodes:
        print(f"{node.value}({node.count})", end=" ")
    print("\n") 