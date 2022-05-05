import unittest
from queue_array import *

class TestLab3(unittest.TestCase):
   
    
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        '''Test queue array init function'''
        q1 = Queue(5)
        self.assertEqual(q1.num_items,0)
        self.assertEqual(q1.items,[None]*5)
        self.assertEqual(q1.front, 0)
        self.assertEqual(q1.rear, 0)
        q2 = Queue(5, [1,2])
        self.assertEqual(q2.num_items,2)
        self.assertEqual(q2.items,[1, 2, None, None, None])
        self.assertEqual(q2.front, 0)
        self.assertEqual(q2.rear, 2)
        
    def test_examples(self):
        q1 = Queue(5)
        self.assertTrue(q1.is_empty())
        self.assertFalse(q1.is_full())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        q2 = Queue(5, [1,2])
        q2.enqueue(3)
        print(q1)
        self.assertEqual(q1, q2)
        
    def test_is_empty(self):
        '''Test queue array is_empty function'''
        q1 = Queue(5)
        q2 = Queue(5, [1])
        self.assertTrue(q1.is_empty())
        self.assertFalse(q2.is_empty())
        
    def test_is_full(self):
        '''Test queue array is_full function'''
        q1 = Queue(2)
        q2 = Queue(2, [1])
        q3 = Queue(2, [1,2])
        self.assertFalse(q1.is_full())
        self.assertFalse(q2.is_full())
        self.assertTrue(q3.is_full())
        
    def test_enqueue(self):
        '''Test queue array enqueue function'''
        q1 = Queue(2)
        self.assertEqual(q1.num_items, 0)
        self.assertEqual(q1.__repr__(), "Queue(2, [])")
        q1.enqueue(5)
        self.assertEqual(q1.num_items, 1)
        self.assertEqual(q1.__repr__(), "Queue(2, [5])")
        q1.enqueue(6)
        self.assertEqual(q1.num_items, 2)
        self.assertEqual(q1.__repr__(), "Queue(2, [5, 6])")
        with self.assertRaises(IndexError): 
            q1.enqueue(7)
    
    def test_dequeue(self):
        '''Test queue array dequeue function'''
        q1 = Queue(2, [1,2])
        self.assertEqual(q1.num_items, 2)
        self.assertEqual(q1.__repr__(), "Queue(2, [1, 2])")
        q1.dequeue()
        self.assertEqual(q1.num_items, 1)
        self.assertEqual(q1.__repr__(), "Queue(2, [2])")
        q1.dequeue()
        self.assertEqual(q1.num_items, 0)
        self.assertEqual(q1.__repr__(), "Queue(2, [])")
        with self.assertRaises(IndexError): 
            q1.dequeue()
            
    def test_size(self):
        '''Test queue array size function'''
        q1 = Queue(5, [1,2,3,4])
        q2 = Queue(5, [1])
        q3 = Queue(5)
        self.assertEqual(q1.size(), 4)
        self.assertEqual(q2.size(), 1)
        self.assertEqual(q3.size(), 0)

if __name__ == '__main__': 
    unittest.main()
