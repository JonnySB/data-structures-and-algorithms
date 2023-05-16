"""
Contains the linked list class
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
        self.length += 1
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
        return temp

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

    def reverse_between(self, m, n):
        if self.length == 0:
            return

        # Edge case, if sublist starts at index 0
        next_is_dummy_head = Node(None)
        next_is_dummy_head.next = self.head
        node_before_sublist = next_is_dummy_head

        for _ in range(m):
            node_before_sublist = node_before_sublist.next

        working_pointer = node_before_sublist.next

        for _ in range(n - m):
            node_to_be_extracted = working_pointer.next
            working_pointer.next = node_to_be_extracted.next
            node_to_be_extracted.next = node_before_sublist.next
            node_before_sublist.next = node_to_be_extracted

        while working_pointer.next:
            working_pointer = working_pointer.next

        self.tail = working_pointer
        self.head = next_is_dummy_head.next

    def partition_list(self, x):
        if not self.head:
            return None

        low_ll_dummy = Node(0)
        high_ll_dummy = Node(0)
        low_ll_previous_node = low_ll_dummy
        high_ll_previous_node = high_ll_dummy
        current_node = self.head

        while current_node:
            if current_node.value < x:
                low_ll_previous_node.next = current_node
                low_ll_previous_node = current_node
            else:
                high_ll_previous_node.next = current_node
                high_ll_previous_node = current_node
            current_node = current_node.next

        low_ll_previous_node.next = high_ll_dummy.next
        high_ll_previous_node.next = None

        self.head = low_ll_dummy.next

    def remove_duplicates(self):
        values_set = set()
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.value in values_set:
                previous_node.next = current_node.next
                self.length -= 1
            else:
                values_set.add(current_node.value)
                previous_node = current_node
            current_node = current_node.next


def find_kth_from_end(linked_list, k):
    turtle = hare = linked_list.head
    for _ in range(k):
        if hare is None:
            return None
        hare = hare.next

    while hare:
        turtle = turtle.next
        hare = hare.next

    return turtle
