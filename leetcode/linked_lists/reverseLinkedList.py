"""
Given the head of a singly linked list, reverse the list, and return the 
reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from linkedList import LinkedList

linked_list = LinkedList()
head = [1, 2, 3, 4, 5]
for num in head:
    linked_list.insertAtEnd(num)
linked_list.printLL()


def reverseListIter(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


reverseListIter(linked_list.head)
linked_list.printLL()
