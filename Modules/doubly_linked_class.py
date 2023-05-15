"""
Douely linked list class definition
"""


class Node():
    """
    Node class with a next and previous pointer to add to doubly linked list
    """
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    """Doubly linked list class and associated methods."""

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
