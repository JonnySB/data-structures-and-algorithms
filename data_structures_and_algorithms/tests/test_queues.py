"""
Tests for the queue's class
"""
from unittest import TestCase, main
import sys
sys.path.append('../')
from data_structures_and_algorithms.queues import Queue, Node


class TestNode(TestCase):
    """Test that Nodes are created correctly"""

    def test_node_constructor(self):
        value = 32
        node = Node(value)
        
        self.assertEqual(node.value, value)
        self.assertIsNone(node.next)


class TestQueue(TestCase):
    """Tests for the Queue class"""

    def setUp(self):
        """Set up queue class with 5 nodes from 1-5"""
        queue_list = [1, 2, 3, 4, 5]
        queue = Queue(queue_list[0])
        for item in queue_list[1:]:
            queue.enqueue(item)

        self.queue_list = queue_list
        self.queue = queue

    def test_constructer(self):
        """Tests that a queue is initialised properly with on Node"""
        value = 41
        queue = Queue(value)

        self.assertEqual(queue.first.value, value)
        self.assertIsNone(queue.first.next)
        self.assertEqual(queue.first, queue.last)
        self.assertEqual(queue.length, 1)

    def test_return_as_list(self):
        """Tests returned list is same as setUp list"""
        self.assertEqual(self.queue.return_as_list(), self.queue_list)

    def test_enqueue(self):
        """tests enqueue works correctly - called in setUp"""
        self.assertEqual(self.queue.first.value, self.queue_list[0])
        self.assertEqual(self.queue.length, len(self.queue_list))
        self.assertEqual(self.queue.last.value, self.queue_list[-1])


if __name__ == "__main__":
    main()
