"""
Tests for stacks class
"""
from unittest import TestCase, main
from stacks import Stack

def create_stack_from_list(lst: list) -> Stack:
    """Return stack from list"""
    stack = Stack(lst[0])
    for item in lst[1:]:
        stack.push(item)
    return stack

class TestStack(TestCase):
    """Class containing tests for Stack and its methods"""

    def setUp(self):
        list_to_stack = [1, 2, 3, 4, 5, 6]
        reverse_list = list_to_stack.copy()
        reverse_list.reverse()
        
        self.stack = create_stack_from_list(list_to_stack)
        self.test_list = reverse_list

    def test_stack_initialisation(self):
        """Test stack initialisation with one node is sucessful"""
        stack = Stack(1)
        self.assertIsNotNone(stack)
        self.assertEqual(stack.return_as_list(), [1])

    def test_push(self):
        """test push through the create_stack_from_list helper function"""
        self.assertEqual(self.stack.return_as_list(), self.test_list)
        self.assertEqual(self.stack.height, 6)
        


if __name__ == '__main__':
    main()
