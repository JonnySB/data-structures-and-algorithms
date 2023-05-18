"""
Queue class constructer and associated methods
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """class containing queue and queue methods"""

    def __init__(self, value):
        """Create queue and add first node"""
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def return_as_list(self) -> list:
        """return queue as list"""
        lst = list()
        temp_node = self.first
        while temp_node is not None:
            lst.append(temp_node.value)
            temp_node = temp_node.next
        return lst

    def enqueue(self, value):
        """enqueue (add) item to end of queue"""
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.length += 1

    def dequeue(self) -> Node:
        """dequeue (remove) item from front of list"""
        if self.length == 0:
            return None
        if self.length == 1:
            self.last = None

        temp_node = self.first
        self.first = self.first.next
        temp_node.next = None

        self.length -= 1
        return temp_node
