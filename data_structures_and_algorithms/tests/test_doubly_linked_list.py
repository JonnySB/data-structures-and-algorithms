"""
Test doubly linked list class - added mid way through
developing the doubly linked list class. tested on
return_as_list and used for TDD with remove method.
"""
from unittest import TestCase, main

import sys
sys.path.append('../')
from data_structures_and_algorithms.doubly_linked_list import DoublyLinkedList


def create_dll_from_list(list):
    dll = DoublyLinkedList(list[0])
    for item in list[1:]:
        dll.append(item)
    return dll


class TestDoublyLinkedList(TestCase):
    """tests for doubly linked list """

    def setUp(self):
        """Set up doubly linked list for use in tests"""
        dll_none = DoublyLinkedList(None)
        self.dll_none = dll_none
        self.list_none = [None]

        self.dll_length_1 = DoublyLinkedList(1)
        self.list_length_1 = [1]

        dll_length_5 = DoublyLinkedList(1)
        for value in range(2, 6):
            dll_length_5.append(value)
        self.dll_length_5 = dll_length_5
        self.list_length_5 = [1, 2, 3, 4, 5]

    def test_return_as_list(self):
        """test returned as list with correct values"""
        self.assertEqual(
            self.dll_length_1.return_as_list(),
            self.list_length_1,
            )
        self.assertEqual(
            self.dll_none.return_as_list(),
            self.list_none,
            )
        self.assertEqual(
            self.dll_length_5.return_as_list(),
            self.list_length_5,
            )

    def test_remove_when_index_less_than_zero(self):
        """Tests returns none when index is less than zero"""
        result = self.dll_none.remove(-1)

        self.assertIsNone(result)

    def test_remove_when_index_greater_than_length(self):
        """Tests returns none when index is greater than length"""
        result = self.dll_length_5.remove(5)

        self.assertIsNone(result)

    def test_removed_node(self):
        """Tests removed node's prev.value, value and next.value are correct"""
        index = 2
        result = self.dll_length_5.remove(index)

        self.assertEqual(result.value, self.list_length_5[index])
        self.assertIsNone(result.prev)
        self.assertIsNone(result.next)

    def test_head_node_after_remove(self):
        """Tests head node is correct after removing index of 0"""
        index = 0
        self.dll_length_5.remove(index)
        self.list_length_5.pop(index)
        self.assertEqual(self.dll_length_5.head.value, self.list_length_5[0])
        self.assertIsNone(self.dll_length_5.head.prev)

    def test_tail_node_after_remove(self):
        """Tests tail node is correct after removing last item in LL"""
        self.dll_length_5.remove(4)
        self.assertEqual(self.dll_length_5.tail.value, 4)
        self.assertIsNone(self.dll_length_5.tail.next)

    def test_remove_only_item(self):
        """Tests removing item from dll with only one item"""
        index = 0
        result_dll = self.dll_length_1.remove(index)
        result_list = self.list_length_1.pop(index)

        self.assertEqual(result_dll.value, result_list)
        self.assertIsNone(self.dll_length_1.head)
        self.assertIsNone(self.dll_length_1.tail)
        self.assertEqual(self.dll_length_1.length, 0)

    def test_remove_middle(self):
        """Tests removing dll item"""
        index = 2
        self.dll_length_5.remove(index)
        self.list_length_5.pop(index)
        self.assertEqual(
            self.dll_length_5.return_as_list(),
            self.list_length_5,
            )

    def test_remove_length(self):
        """Tests length after removing ll item"""
        index = 2
        self.dll_length_5.remove(index)
        self.list_length_5.pop(index)
        self.assertEqual(self.dll_length_5.length, len(self.list_length_5))

    def test_swap_first_and_last(self):
        """Test swapping first and last value"""
        self.dll_length_5.swap_first_last()
        self.assertEqual(self.dll_length_5.return_as_list(), [5, 2, 3, 4, 1])

    def test_is_palindrome(self):
        """Test whether list is palidrome"""
        dll = create_dll_from_list([1, 2, 3, 4, 3, 2, 1])
        self.assertTrue(dll.is_palindrome())

        dll = create_dll_from_list([1, 2, 3, 3, 2, 1])
        self.assertTrue(dll.is_palindrome())

        dll = create_dll_from_list([1, 2, 3, 4, 3, 2])
        self.assertFalse(dll.is_palindrome())

        dll = create_dll_from_list([1])
        dll.pop()
        self.assertTrue(dll.is_palindrome())

    def test_swap_pairs(self):
        """Tests swap pairs and len 0 & 1 edge cases"""

        dll = create_dll_from_list([1, 2, 3, 4])
        dll.swap_pairs()
        self.assertEqual(dll.return_as_list(), [2, 1, 4, 3])

        dll = create_dll_from_list([1, 2, 3, 4, 5])
        dll.swap_pairs()
        self.assertEqual(dll.return_as_list(), [2, 1, 4, 3, 5])


if __name__ == '__main__':
    main()
