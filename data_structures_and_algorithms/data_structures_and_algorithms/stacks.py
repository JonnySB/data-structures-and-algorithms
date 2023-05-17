"""
Stacks class
"""

class Node():
    """Class for instantiating Linked List nodes"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    """Class for implementing a stack data structure"""

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def return_as_list(self):
        """Return stack as list with top item on left (LIFO)"""
        return_list = []
        temp = self.top
        while temp is not None:
            return_list.append(temp.value)
            temp = temp.next
        return return_list

    def push(self, value):
        """Add value to top of stack"""
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        """pop node from top of stack and return it"""
        if self.height == 0:
            return None
        temp_node = self.top
        self.top = self.top.next
        temp_node.next = None
        self.height -= 1
        return temp_node



    
