'''
Queue: Linear data structure that operates as FIFO
Queue has two major functions: enqueue and dequeue
Queue Implementation:
    1. Using List
    2. Using LinkedList
'''

# Implementation using list
class ListQueue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value: any) -> None:
        self.queue.append(value)

    def dequeue(self) -> any:
        try:
            return self.queue.pop(0)
        except IndexError:
            raise

    def print_queue(self) -> None:
        for value in self.queue:
            print(value)
        print('\n')

# Implementation using Doubly LinkedList
class QueueNode:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None
        self.prev = None

class LinkedListQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def enqueue(self, value: any) -> None:
        new_node = QueueNode(value)
        if self.head is None:
            self.head = new_node
        elif self.tail is None:
            self.tail = new_node
            self.head.prev = self.head.next =self.tail
            self.tail.prev = self.tail.next = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node


    def dequeue(self) -> any:
        if self.head is None:
            raise Exception("Queue is empty.")
        curr_head = self.head
        curr_head_value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = self.tail
            self.tail.next = self.head
        curr_head.value, curr_head.next, curr_head.prev = None , None, None
        return curr_head_value


    def print_queue(self) -> None:
        if self.head is None:
            print("")
            return
        print(self.head.value)
        curr_node = self.head.next
        while curr_node is not self.head:
            print(curr_node.value)
            curr_node = curr_node.next


# # Driver code
# list_queue = ListQueue()
# list_queue.enqueue(1)
# list_queue.enqueue(2)
# list_queue.enqueue(3)
# list_queue.enqueue(4)
# list_queue.print_queue()
# list_queue.dequeue()
# list_queue.dequeue()
# list_queue.print_queue()

ll_queue = LinkedListQueue()
ll_queue.print_queue()
print("-----")
ll_queue.enqueue(1)
ll_queue.enqueue(2)
ll_queue.enqueue(3)
ll_queue.enqueue(4)
ll_queue.print_queue()
print("-----")
ll_queue.dequeue()
ll_queue.print_queue()
print("-----")


