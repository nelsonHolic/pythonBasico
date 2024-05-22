# Python program to demonstrate
# queue implementation using a linked list.
# node class
from typing import Optional


class Node:
    next: Optional['Node']

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    size: int
    front: Optional[Node]
    back: Optional[Node]
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    # String representation of the stack
    def __str__(self):
        node = self.front
        out = ""
        while node:
            out += f"{node.value}"

            if node.next is not None:
                out += "->"
            node = node.next
        return "back-> " + out + " <-front"

    # Get the current size of the stack
    def get_size(self) -> int:
        return self.size

    # Check if the stack is empty
    def is_empty(self) -> bool:
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.front.next.value

    # Enqueue a value into the queue.
    def enqueue(self, value) -> None:
        node = Node(value)

        if self.is_empty():
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node
        self.size += 1

    # Remove a value from the stack and return.
    def dequeue(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.front
        self.front = self.front.next
        self.size -= 1
        return remove.value


# Driver Code
if __name__ == "__main__":
    queue = Queue()

    print("--------------------------- enqueue ---------------------")
    for i in range(1, 11):
        print(queue)
        queue.enqueue(i)
    print(f"Queue: {queue}")

    print("--------------------------- dequeue ---------------------")

    for _ in range(1, 6):
        print(queue)
        remove = queue.dequeue()
        print(f"Dequeue: {remove}")
    print(f"Queue: {queue}")
