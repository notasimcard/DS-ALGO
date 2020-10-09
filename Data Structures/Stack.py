'''
Implementation of stack in python:
    1. Using list
        - use append() to add element to the list
        - use pop() to take element out of the list to remove elements in LIFO order
        - downsides:
            - The items are stored next to each other in memory, so if the stack grows bigger than the 
                memory, then Python needs to do some memory allocations
            - List in python is implemented as dynamic array. So if the list gets full it needs to resize.
                So, the O(1) complexity is not 100% consistent
        - benefits:
            - You can access elements with O(1) if using list
    2. Using collections.deque (pronounced as deck)
        - Faster appends and pop on both ends
        - Uniform O(1) complexity for pop, append
        - Deque in python is implemented using doubly linked list
    3. Using LIFO queue
        - Time complexity for insert, remove is O(1)
''' 

from collections import deque
from queue import LifoQueue

class Stack:
    def __init__(self):
        self.stack = []


    def push(self, data):
        self.stack.append(data)


    def peek(self):
        return self.stack[-1]


    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()


    def empty(self):
        return len(self.stack) == 0


    def size(self):
        return len(self.stack)

# # Driver code
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.size())
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack.empty())
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())

# # Stack with deque driver code
stack_deque = deque()
# stack_deque.append(1)
# stack_deque.append(2)
# stack_deque.append(3)
# stack_deque.append(4)
# stack_deque.append(5)
# print(stack_deque)
# stack_deque.pop()
# print(stack_deque)

# LIFO queue
stack_q = LifoQueue()
# stack_q.put(1)
# stack_q.put(2)
# stack_q.put(3)
# stack_q.put(4)
# stack_q.put(5)
# print(stack_q.get())
# print(stack_q.get())
# print(stack_q.get())
# print(stack_q.get())
# print(stack_q.get())
# print(stack_q.empty())




