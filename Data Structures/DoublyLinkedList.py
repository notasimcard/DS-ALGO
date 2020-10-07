class DLLNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class DoublyLL():
    def __init__(self):
        self.head = None
        self.tail = None


    def add_node(self, val):
        new_node = DLLNode(val)
        if not self.head:
            self.head = self.tail = new_node
        elif self.head == self.tail:
            self.tail = new_node
            self.head.right = self.head.left = self.tail
            self.tail.right = self.tail.left = self.head
        else:
            self.tail.right = new_node
            self.head.left = new_node
            new_node.left = self.tail
            new_node.right = self.head
            self.tail = new_node


    def print_list(self, reversed=False):
        if not self.head:
            return

        if reversed:
            curr = self.tail
            while curr != self.head:
                print(curr.val)
                curr = curr.left
        else:
            curr = self.head
            while curr != self.tail:
                print(curr.val)
                curr = curr.right
        print(curr.val)


    def remove(self, del_val):  
        # case 1: list is empty
        if not self.head:
            return

        # case 2: del_val is the only element
        if self.head == self.tail and self.head.val == del_val:
            self.head = None
            self.tail = None
            return self.head

        # case 3: del_val
        curr = self.head
        prev = self.tail

        while True:
            if curr.val == del_val:
                if curr == self.head:
                    self.head = curr.right
                if curr == self.tail:
                    self.tail = curr.left
                prev.right = curr.right
                curr.right.left = prev
                curr.val = curr.left = curr.right = None
                return
            prev = curr
            curr = curr.right
            # case 4: no del_val in list
            if curr == self.head:
                print(f"Value {del_val} not found.")
                return 

# driver code
double_ll = DoublyLL()
double_ll.add_node(1)
double_ll.add_node(2)
double_ll.add_node(3)
double_ll.add_node(4)
double_ll.add_node(5)
double_ll.print_list()
print('----------------')
double_ll.print_list(reversed=True)
print('----------------')
double_ll.remove(5)
double_ll.remove(4)
double_ll.remove(3)
double_ll.remove(2)
double_ll.remove(1)
double_ll.print_list()
print('----------------')
