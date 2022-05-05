import unittest

from queue_nodelist import *

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue()
        q.is_empty()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        '''Test init function for Queue object'''
        q1 = Queue()
        self.assertEqual(q1.num_items,0)
        self.assertEqual(q1.front, None)
        self.assertEqual(q1.rear, None)

    def test_examples(self):
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        self.assertFalse(q1.is_empty())
        self.assertEqual(q1.size(), 3)
        self.assertEqual(q1.dequeue(),1)
        q2 = Queue()
        q2.enqueue(2)
        q2.enqueue(3)
        self.assertEqual(q1, q2)
        
    def test_is_empty(self):
        '''Test is_empty function for Queue object'''
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        q1.enqueue(1)
        self.assertFalse(q1.is_empty())
        
    def test_enququq(self):
        '''Test enqueue function for Queue object'''
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        self.assertEqual(q1.get_items(), [])
        
        q1.enqueue(10)
        self.assertEqual(q1.front.value, 10)
        self.assertEqual(q1.rear.value, 10)
        self.assertEqual(q1.get_items(), [10])
        
        q1.enqueue(20)
        self.assertEqual(q1.front.value, 10)
        self.assertEqual(q1.rear.value, 20)
        self.assertEqual(q1.get_items(), [10,20])
        
        q1.enqueue(30)
        self.assertEqual(q1.front.value, 10)
        self.assertEqual(q1.rear.value, 30)
        self.assertEqual(q1.get_items(), [10,20,30])
        
        q1.enqueue(40)
        self.assertEqual(q1.front.value, 10)
        self.assertEqual(q1.rear.value, 40)
        self.assertEqual(q1.get_items(), [10,20,30,40])
        
    def test_dequeue(self):
        '''Test dequeue function for Queue object'''
        q1 = Queue()
        q1.enqueue(10)
        q1.enqueue(20)
        q1.enqueue(30)
        self.assertEqual(q1.front.value, 10)
        self.assertEqual(q1.rear.value, 30)
        self.assertEqual(q1.get_items(), [10,20,30])
        
        self.assertEqual(q1.dequeue(), 10)
        self.assertEqual(q1.front.value, 20)
        self.assertEqual(q1.rear.value, 30)
        self.assertEqual(q1.get_items(), [20,30])
        
        self.assertEqual(q1.dequeue(), 20)
        self.assertEqual(q1.front.value, 30)
        self.assertEqual(q1.rear.value, 30)
        self.assertEqual(q1.get_items(), [30])
  
        self.assertEqual(q1.dequeue(), 30)
        self.assertEqual(q1.front, None)
        self.assertEqual(q1.rear, None)
        self.assertEqual(q1.get_items(), [])
        
        with self.assertRaises(IndexError): 
            q1.dequeue()
        
    def test_size(self):
        '''Test size function for Queue object'''
        q1 = Queue()
        self.assertEqual(q1.size(), 0)
        q1.enqueue(1)
        self.assertEqual(q1.size(), 1)
        q1.enqueue(2)
        self.assertEqual(q1.size(), 2)
        q1.dequeue()
        self.assertEqual(q1.size(), 1)
        q1.dequeue()
        self.assertEqual(q1.size(), 0)

if __name__ == '__main__': 
    unittest.main()