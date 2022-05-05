import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self):
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self):
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_is_empty(self):
        # Test is_empty on non-empty stacks
        stack1 = Stack(Node(2, Node(1, None)))
        self.assertEqual(stack1.is_empty(), False)
        stack2 = Stack(Node(1, None))
        self.assertEqual(stack2.is_empty(), False)
        # Test is_empty on empty stack
        stack3 = Stack(None)
        self.assertEqual(stack3.is_empty(), True)
    
    def test_push(self):
        # Test push on a stack
        stack1 = Stack()
        self.assertEqual(stack1, Stack())
        stack1.push(1)
        self.assertEqual(stack1, Stack(Node(1, None)))
        stack1.push(2)
        self.assertEqual(stack1, Stack(Node(2, Node(1, None))))

    def test_pop(self):
        stack1 = Stack(Node(1, Node(2, None)))
        # Test pop on a stack
        self.assertEqual(stack1.pop(), 1)
        # Test pop on same stack
        self.assertEqual(stack1.pop(), 2)
        # Test pop on same stack (now empty)
        with self.assertRaises(IndexError):
            stack1.pop()

    def test_peek(self):
        stack1 = Stack(Node(1, Node(2, None)))
        # Test peek on a stack
        self.assertEqual(stack1.peek(), 1)
        stack2 = Stack()
        # Test pop on an empty stack
        with self.assertRaises(IndexError):
            stack2.peek()

if __name__ == '__main__': 
    unittest.main()
