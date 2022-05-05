import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_is_empty(self):
        # Test is_empty on non-empty stacks
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.is_empty(), False)
        stack2 = Stack(3, ["nice", "interesting", "what?"])
        self.assertEqual(stack2.is_empty(), False)
        # Test is_empty on empty stacks
        stack3 = Stack(10)
        self.assertEqual(stack3.is_empty(), True)
        stack4 = Stack(3, [])
        self.assertEqual(stack4.is_empty(), True)

    def test_is_full(self):
        # Test is_full on non-full stacks
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.is_full(), False)
        stack2 = Stack(10)
        self.assertEqual(stack2.is_full(), False)
        # Test is_full on full stacks
        stack3 = Stack(3, ["nice", "interesting", "what?"])
        self.assertEqual(stack3.is_full(), True)
        stack4 = Stack(4, [9,13,2,1])
        self.assertEqual(stack4.is_full(), True)
    
    def test_push(self):
        # Test push on a valid stack
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")
        self.assertEqual(stack.num_items, 2)
        stack.push(12)
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2, 12])")
        self.assertEqual(stack.num_items, 3)
        # Test push on a valid stack
        stack = Stack(3)
        self.assertEqual(stack.__repr__(), "Stack(3, [])")
        self.assertEqual(stack.num_items, 0)
        stack.push(1)
        self.assertEqual(stack.__repr__(), "Stack(3, [1])")
        self.assertEqual(stack.num_items, 1)
        # Test push on a full stack
        with self.assertRaises(IndexError):
            stack1 = Stack(5, [1, 2, 3, 4, 5])
            stack1.push(6)

    def test_pop(self):
        stack1 = Stack(5, [1, 2])
        # Test pop on valid stack
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.__repr__(), "Stack(5, [1])")
        # Test pop again on same stack
        self.assertEqual(stack1.pop(), 1)
        self.assertEqual(stack1.__repr__(), "Stack(5, [])")
         # Test pop again on same stack (now empty)
        with self.assertRaises(IndexError):
            stack1.pop()
    
    def test_peek(self):
        # Test peek on a valid stack
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.peek(), 2)
        # Test peek on a valid stack
        stack2 = Stack(10, [1, 2, 14, -5])
        self.assertEqual(stack2.peek(), -5)
        # Test peek on an empty stack
        stack3 = Stack(5)
        with self.assertRaises(IndexError):
            stack3.peek()
    
    def test_size(self):
        # Test size on a semi-full stack
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.size(), 2)
        # Test size on a full stack
        stack2 = Stack(4, [1, 2, 3, 4])
        self.assertEqual(stack2.size(), 4)
        # Test size on an empty stack
        stack3 = Stack(7, [])
        self.assertEqual(stack3.size(), 0)

if __name__ == '__main__': 
    unittest.main()
