
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



    # Create new node and insert node 
    def insert(self, index, value):
        pass



my_linked_list = LinkedList(4)

my_linked_list.append(5)

my_linked_list.append(3)

my_linked_list.append(1)

my_linked_list.append(2)

my_linked_list.print_as_list()

print(my_linked_list.pop().value)

my_linked_list.print_as_list()

my_linked_list.prepend(3)

my_linked_list.print_as_list()

print(my_linked_list.pop_first())

my_linked_list.print_as_list()