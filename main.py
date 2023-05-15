"""
Test area to run modules / funcs from data structures and algoritms course
"""

from Modules.doubly_linked_class import DoublyLinkedList


def main():
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.print_as_list()
    popped_node = my_doubly_linked_list.pop()
    print(popped_node)
    my_doubly_linked_list.print_as_list()
    my_doubly_linked_list.prepend(0.5)
    my_doubly_linked_list.print_as_list()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_as_list()
    print(my_doubly_linked_list.length)
    print(my_doubly_linked_list.get(1).value)
    print(my_doubly_linked_list.get(3).value)
    print(my_doubly_linked_list.get(5))


if __name__ == "__main__":
    main()
