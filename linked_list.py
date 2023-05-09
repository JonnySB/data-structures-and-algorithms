"""
Linked List Module containing linked list class with
associated basic function methods and common interveriw style
questions.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        """Create new node"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_as_list(self):
        """Print list"""
        lst = []
        temp = self.head
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        print(lst)

    def append(self, value):
        """Create new node and add to the end"""
        new_node = Node(value)
        if self.head is None:  # Edge case - if initialising
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove and return last item from list"""
        if self.length == 0:  # Edge case - empty list
            return None
        # Search though LL and set second to last to none
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1  # Edge case - was only 1 item
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        """Create new node and add to the beginning"""
        new_node = Node(value)
        if self.length == 0:  # If list is empty
            self.head = new_node
            self.tail = new_node
        else:  # If list is not empty
            new_node.next = self.head
            self.head = new_node
        return True

    def pop_first(self):
        if self.length == 0:  # Edge case: 0 items in list
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:  # Edge case: 1 item list
            self.tail = None
        return temp.value

    def get(self, index):
        if index >= self.length or index < 0:  # Edge cases
            return None
        else:  # Get node at index
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:  # Same as is not none
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Create new node and insert node"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while True:
            if fast is None or fast.next is None:
                return slow
            else:
                slow = slow.next
                fast = fast.next.next

    def has_loop(self):
        slow = self.head
        fast = self.head
        counter = 0
        while True:
            if fast is None or fast.next is None:
                return False
            if slow is fast and counter > 0:
                return True
            counter += 1
            slow = slow.next
            fast = fast.next.next

    def find_kth_from_end(self, k):
        slow = self.head
        fast = self.head
        for _ in range(k):
            pass


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.print_as_list()
