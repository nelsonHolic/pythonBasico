# Python program to demonstrate
# stack implementation using a linked list.
# node class
from typing import Optional


class Node:
    next: Optional['Node']

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        node = self.head.next
        out = ""
        while node:
            out += str(node.value) + "->"
            node = node.next
        return "Head->" + out

    # Get the current size of the stack
    def get_size(self):
        return self.size

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


# Driver Code
if __name__ == "__main__":
    stack = Stack()

    print("--------------------------- push ---------------------")
    for i in range(1, 11):
        print(stack)
        stack.push(i)
    print(f"Stack: {stack}")

    print("--------------------------- pop ---------------------")

    for _ in range(1, 6):
        print(stack)
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
