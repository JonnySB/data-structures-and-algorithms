"""
Douely linked list class definition
"""


class Node():
    """
    Node class with a next and previous pointer to add to doubly linked list
    """
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly linked list class and associated methods."""

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_as_list(self):
        """Prints doubly linked list as list"""
        temp_node = self.head
        temp_list = []
        while temp_node is not None:
            temp_list.append(temp_node.value)
            temp_node = temp_node.next
        print(temp_list)

    def append(self, value):
        """Appends value to end of doubly linked list and returns true"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Pops last node off doubly linked list and returns it"""
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        """prepend node to beginning of doubly linked list"""
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """Pop first node from doubly linked list and return it"""
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """Get node at given index"""
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1, index):
                temp = temp.prev
            return temp
