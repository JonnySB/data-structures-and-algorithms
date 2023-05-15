"""
Functions to work with the linked list class
"""


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
