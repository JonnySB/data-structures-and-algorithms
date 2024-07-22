"""
Doubely linked list class definition
"""


def funct(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
          sixteen, seventeen):
    pass


class Node:
    """
    Node class with a next and previous pointer to add to doubly linked list - this is a very long coment meant to trigger the auto formatting
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

    def return_as_list(self) -> list:
        """Prints doubly linked list as list"""
        temp_node = self.head
        temp_list = []
        while temp_node is not None:
            temp_list.append(temp_node.value)
            temp_node = temp_node.next
        return temp_list

    def append(self, value) -> bool:
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

    def pop(self) -> Node:
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

    def prepend(self, value) -> bool:
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

    def pop_first(self) -> Node:
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

    def get(self, index: int) -> Node:
        """Get node at given index"""
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1, index):
                temp = temp.prev
            return temp

    def set_value(self, index: int, value) -> bool:
        """Sets value at given index and returns bool"""
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def insert(self, index: int, value) -> bool:
        """
        Inserts node at given index, or returns None if out of index bounds
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev_node = self.get(index - 1)
        next_node = prev_node.next

        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node

        self.length += 1
        return True

    def remove(self, index: int) -> Node:
        """Remove and return node at given index"""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp_node = self.get(index)

        temp_node.next.prev = temp_node.prev
        temp_node.prev.next = temp_node.next
        temp_node.prev = None
        temp_node.next = None

        self.length -= 1
        return temp_node

    def swap_first_last(self):
        "Swap head and tail values"
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def reverse(self):
        """Reverse doubly linked list"""
        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    def is_palindrome(self):
        if self.length <= 1:
            return True
        temp_front = self.head
        temp_back = self.tail
        for _ in range(self.length // 2):
            if temp_front.value == temp_back.value:
                temp_front = temp_front.next
                temp_back = temp_back.prev
            else:
                return False
        return True

    def swap_pairs(self):
        """Swap pairs by iterating through using a train of three Nodes"""
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while self.head and self.head.next:
            first = self.head
            second = self.head.next

            prev.next = second
            first.next = second.next
            second.next = first

            second.prev = prev
            first.prev = second
            if first.next:
                first.next.prev = first

            self.head = first.next
            prev = first

        self.head = dummy.next
        if self.head:
            self.head.prev = None
