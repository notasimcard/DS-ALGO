"""
    implementation of singly linked list
"""

class SingleLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None


    def addNode(self, value):
        new_node = SingleLLNode(value)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node


    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next


    def delete_node(self, del_value):
        # case 1: LL is null
        if not self.head:
            return


        # case 2: head has the delete value
        if self.head.value == del_value:
            self.head = self.head.next
            return

        # case 3: delete value is in other nodes beside head
        curr = self.head.next
        last_node = self.head
        while curr:
            if curr.value == del_value:
                last_node.next = curr.next
                curr.next = None
                return
            last_node = curr
            curr = curr.next
        # case 4: no delete value
        print(f"{del_value} is not in the list.")
        return


def reverse_LL(linked_list):
    if not linked_list.head:
        print("The list is empty.")
        return

    if not linked_list.head.next:
        return linked_list

    curr_node = linked_list.head
    last_node = None    
    while curr_node:
        next_node = curr_node.next
        curr_node.next = last_node
        last_node = curr_node
        curr_node = next_node

    linked_list.head = last_node

# driver code
single_LL = SingleLL()
single_LL.addNode(1)
single_LL.print_list()
print('----------------')
single_LL.addNode(2)
single_LL.addNode(3)
single_LL.print_list()
print('----------------')
single_LL.delete_node(2)
single_LL.print_list()
print('----------------')
single_LL.addNode(5)
single_LL.addNode(6)
reverse_LL(single_LL)
single_LL.print_list()
print('----------------')
reverse_LL(single_LL)
single_LL.print_list()
print('----------------')
single_LL.delete_node(5)
single_LL.delete_node(1)
single_LL.delete_node(10)
print('----------------')
single_LL.print_list()
