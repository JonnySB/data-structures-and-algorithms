'''
Merge Two Sorted LL ( ** Interview Question)
Description
The merge method takes in another LinkedList as an input and merges it with the current LinkedList. The elements in both lists are assumed to be in ascending order, but the input lists themselves do not need to be sorted.

Parameters
other_list (LinkedList): the other LinkedList to merge with the current list

Return Value
This method does not return a value, but it modifies the current LinkedList to contain the merged list.

Example:

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)
 
l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)
 
l1.merge(l2)
 
# The current list (l1) now contains the merged list [1, 2, 3, 4, 5, 6, 7, 8]

Details
The merge method works as follows:
It gets the head node of the other linked list (other_list.head) and sets it to a local variable called other_head.
It creates a new node called dummy with a value of 0, which will serve as the head of the merged linked list.
It creates a new node called current and sets it equal to `
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0)
        current = dummy

        while self.head is not None and other_head is not None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next
        
        if self.head is not None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail
            
        self.head = dummy.next
        self.length += other_list.length

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
