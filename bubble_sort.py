# Initialise the Node
import random
import time


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

# Class for doubly Linked List
class DoubleLinkedList:
    def __init__(self):
        self.start_node = None

    def __str__(self):
        node = self.start_node
        out = ""
        while node:
            out += f"{node.value}"

            if node.next is not None:
                out += "<->"
            node = node.next
        return out

    # Insert element at the end
    def insert_to_end(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n


    # Delete the elements from the start
    def insert_at(self, val, index: int):
        new_node = Node(val)

        count = 0
        current = self.start_node

        while current:
            if count == index:
                if current.next:
                    new_node.next = current.next
                    current.next = new_node
                    new_node.prev = new_node.next.prev
                    new_node.next.prev = new_node
                else:
                    current.next = new_node
                    new_node.prev = current

            else:
                current = current.next

            count += 1


    # Delete the elements from the start
    def delete_at(self, index: int):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return

        count = 0
        current = self.start_node

        while current:
            if count == index:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev

                return current
            else:
                current = current.next
            count += 1

    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def bubble_sort(self):
        # If the list is empty or has only one element, it's already sorted
        if self.start_node is None or self.start_node.next is None:
            return

        # Flag to check if any swaps have been made in a pass
        swapped = True

        # Perform the bubble sort
        while swapped:
            swapped = False
            current = self.start_node
            while current.next is not None:
                if current.value > current.next.value:
                    # Swap nodes
                    if current.prev:
                        current.prev.next = current.next
                    else:
                        self.start_node = current.next
                    current.next.prev = current.prev
                    current.prev = current.next
                    current.next = current.next.next
                    current.prev.next = current
                    if current.next:
                        current.next.prev = current
                    swapped = True
                else:
                    current = current.next

# Example usage:
dll = DoubleLinkedList()
dll.insert_to_end(5)
dll.insert_to_end(3)
dll.insert_to_end(8)
dll.insert_to_end(1)

start = time.time()
print("Before sorting:", dll)
dll.bubble_sort()
print("After sorting:", dll)
print(f"Esto es lo que se demora: {time.time() - start}")


dll2 = DoubleLinkedList()

for i in range(10000):
    dll2.insert_to_end(random.randint(1,10000))

start = time.time()
dll2.bubble_sort()
print(f"Esto es lo que se demora: {time.time() - start}")

list_dd = []

for i in range(10_000_000):
    list_dd.append(random.randint(1,100_000))

start = time.time()
list_dd.sort()
print(f"Esto es lo que se demora: {time.time() - start}")

