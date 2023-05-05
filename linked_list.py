
# LinkedList

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    
    # Create new node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    # Print list
    def print_as_list(self):
        lst = []
        temp = self.head
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        print(lst)


    # Create new node and add to the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None: # Edge case - if initialising
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Remove and return last item from list
    def pop(self):
        if self.length == 0: # Edge case - empty list
            return None
        # Search though LL and set second to last to none
        temp = self.head
        pre = self.head
        while (temp.next):
                pre = temp
                temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1 # Edge case - was only 1 item
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    

    # Create new node and add to the beginning
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0: # If list is empty
            self.head = new_node
            self.tail = new_node
        else: # If list is not empty
            new_node.next = self.head
            self.head = new_node
        return True


    def pop_first(self):
        if self.length == 0: # Edge case: 0 items in list
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0: # Edge case: 1 item list
            self.tail = None
        return temp.value


    def get(self, index):
        if index >= self.length or index < 0: #Edge cases
            return None
        else: # Get node at index
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp: # same as is not none
            temp.value = value
            return True
        return False
        
    # Create new node and insert node 
    def insert(self, index, value):
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
        pass





my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.append(3)

my_linked_list.append(4)

my_linked_list.append(5)

my_linked_list.reverse()

my_linked_list.print_as_list()
