"""

Bubble Sort of LL ( ** Interview Question)
Assignment:

Write a bubble_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the bubble sort algorithm. The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.



Input:

The LinkedList object containing a linked list with unsorted elements (self).



Output:

None. The method sorts the linked list in place.



Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.

The bubble sort algorithm works by repeatedly iterating through the unsorted part of the list, comparing adjacent elements and swapping them if they are in the wrong order.

The method starts with the entire linked list being the unsorted part of the list.

For each pass through the unsorted part of the list, the method iterates through each pair of adjacent elements and swaps them if they are in the wrong order.

After each pass, the largest element in the unsorted part of the list will "bubble up" to the end of the list.

The method continues iterating through the unsorted part of the list until no swaps are made during a pass.

After the linked list is fully sorted, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.



Constraints:

The linked list can contain duplicates.

The method should be implemented in the LinkedList class.

The method should not use any additional data structures to sort the linked list.

"""


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

    def print_as_list(self):
        lst = []
        temp = self.head
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        return lst

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    """
    Linked list bubble sort trick:
        - For each pass through, set a sorted_until marker working incrementally from the 
        end to the beginning of the list. This can then control when the inner loop should 
        stop (current.next = sorted_until) and the outer loop is finished (self.head.next = sorted_until)

    """

    def bubble_sort(self):
        if self.length < 2:
            return
        sorted_until = None
        while self.head.next != sorted_until:
            current = self.head
            while current.next != sorted_until:
                next = current.next
                if current.value > next.value:
                    current.value, next.value = next.value, current.value
                current = current.next
            sorted_until = current

    """
    Bubble sort but actually swapping the nodes rather than just updating their values:
    """

    def swap_nodes(self, x, y):
        if x == y:
            return

        # find x node whilst keeping track of prev
        prev_x = None
        curr_x = self.head
        while curr_x is not None and curr_x.value != x:
            prev_x = curr_x
            curr_x = curr_x.next

        # repeat for y
        prev_y = None
        curr_y = self.head
        while curr_y is not None and curr_y.value != y:
            prev_y = curr_y
            curr_y = curr_y.next

        # if x or curr_y doesn't exist:
        if curr_x is None or curr_y is None:
            return

        # if x is head, make y head
        if prev_x is not None:
            prev_x.next = curr_y
        else:
            self.head = curr_y

        # repeat for y
        if prev_y is not None:
            prev_y.next = curr_x
        else:
            self.head = curr_x

        # swap next pointers
        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp

    def bubble_sort_swapping_nodes(self):
        if self.length < 2:
            return
        sorted_until = None
        while self.head.next != sorted_until:
            current = self.head
            while current.next != sorted_until:
                next = current.next
                if current.value > next.value:
                    self.swap_nodes(current.value, next.value)
                else:
                    current = current.next
            sorted_until = current


my_linked_list = LinkedList(6)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(4)
my_linked_list.append(1)
my_linked_list.append(7)
my_linked_list.append(3)

print("Linked List Before Sort:")
print(my_linked_list.print_as_list())

my_linked_list.bubble_sort_swapping_nodes()

print("\nSorted Linked List:")
print(my_linked_list.print_as_list())
