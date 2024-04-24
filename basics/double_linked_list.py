# Initialise the Node
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


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

# Create a double linked list object
dll = DoubleLinkedList()

# Insert elements to the end of the list
dll.insert_to_end(1)
dll.insert_to_end(2)
dll.insert_to_end(3)

# Print the initial state of the list
print("Initial List:", dll)



dll.insert_at(10, 1)

# Print the initial state of the list
print("List after insert:", dll)

# Delete element at index 1
dll.delete_at(1)

# Print the list after deletion
print("List after deleting element at index 1:", dll)

# Delete element at the end
dll.delete_at_end()

# Print the list after deleting the last element
print("List after deleting element at the end:", dll)

