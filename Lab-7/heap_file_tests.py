import unittest
from heap import *

class TestLab7(unittest.TestCase):
    
    def test_01_init(self):
        h = MaxHeap()
        self.assertEqual(h.cap, 50)
        self.assertEqual(h.num_items, 0)
        self.assertEqual(h.last_idx, 0)
        self.assertEqual(h.heap, [None]*51)
        
    def test_02_enqueue(self):
        h = MaxHeap(4)
        h.enqueue(10)
        self.assertEqual(h.num_items, 1)
        self.assertEqual(h.heap[1], 10)
        h.enqueue(5)
        self.assertEqual(h.num_items, 2)
        self.assertEqual(h.heap[2], 5)
        h.enqueue(15)
        self.assertEqual(h.num_items, 3)
        self.assertEqual(h.heap[1], 15)
        self.assertEqual(h.heap[2], 5)
        self.assertEqual(h.heap[3], 10)
        h.enqueue(25)
        self.assertEqual(h.num_items, 4)
        self.assertEqual(h.heap[1], 25)
        self.assertEqual(h.heap[2], 15)
        self.assertEqual(h.heap[3], 10)
        self.assertEqual(h.heap[4], 5)

        with self.assertRaises(IndexError): 
            h.enqueue(5)
        
    def test_03_peek(self):
        h = MaxHeap()
        with self.assertRaises(IndexError): 
            h.peek()
        h.enqueue(10)
        self.assertEqual(h.peek(), 10)
        h.enqueue(5)
        self.assertEqual(h.peek(), 10)
        h.enqueue(15)
        self.assertEqual(h.peek(), 15)
    
    def test_04_dequeue(self):
        h = MaxHeap()
        heap = [82,65,71,55,48,41,42,38,23,26,37,25]
        for item in heap:
            h.enqueue(item)
        self.assertEqual(h.heap[1:13], [82,65,71,55,48,41,42,38,23,26,37,25])
        self.assertEqual(h.dequeue(), 82)
        self.assertEqual(h.heap[1:12], [71,65,42,55,48,41,25,38,23,26,37])
        self.assertEqual(h.dequeue(), 71)
        self.assertEqual(h.heap[1:11], [65,55,42,38,48,41,25,37,23,26])
        self.assertEqual(h.dequeue(), 65)
        self.assertEqual(h.heap[1:10], [55,48,42,38,26,41,25,37,23])
        self.assertEqual(h.dequeue(), 55)
        self.assertEqual(h.heap[1:9], [48,38,42,37,26,41,25,23])
        
    def test_05_contents(self):
        h1 = MaxHeap(5)
        h2 = MaxHeap(5)
        h3 = MaxHeap(5)
        heap1 = [1,2,3,4,5]
        for item in heap1:
            h1.enqueue(item)
        h2.enqueue(1)
        self.assertEqual(h1.contents(), [5,4,2,1,3])
        self.assertEqual(h2.contents(), [1])
        self.assertEqual(h3.contents(), [])
        
    def test_06_build_heap(self):
        h1 = MaxHeap(5)
        h1.build_heap([1,2,3,4,5])
        self.assertEqual(h1.contents(), [5,4,3,1,2])
        h2 = MaxHeap(7)
        h2.build_heap([6,4,2,1,8,9,3])
        self.assertEqual(h2.contents(), [9,8,6,1,4,2,3])
    
    def test_07_is_empty(self):
       h1 = MaxHeap(2)
       self.assertTrue(h1.is_empty())
       h1.enqueue(1)
       self.assertFalse(h1.is_empty())
    
    def test_08_is_full(self):
       h1 = MaxHeap(2)
       self.assertFalse(h1.is_full())
       h1.enqueue(1)
       self.assertFalse(h1.is_full())
       h1.enqueue(2)
       self.assertTrue(h1.is_full())
    
    def test_09_capacity(self):
        h1 = MaxHeap(2)
        h2 = MaxHeap(5)
        h3 = MaxHeap(20)
        self.assertEqual(h1.capacity(), 2)
        self.assertEqual(h2.capacity(), 5)
        self.assertEqual(h3.capacity(), 20)
        
    def test_10_size(self):
        h1 = MaxHeap(10)
        self.assertEqual(h1.size(), 0)
        h1.enqueue(1)
        h1.enqueue(2)
        self.assertEqual(h1.size(), 2)
        h1.enqueue(3)
        h1.enqueue(4)
        self.assertEqual(h1.size(), 4)

    def test_11_perc_down(self):
        h1 = MaxHeap(10)
        h1.heap = [None,1,2,3]
        h1.num_items = 3
        h1.perc_down(1)
        h1.contents()
        self.assertEqual(h1.contents(), [3,2,1])
    
    def test_12_perc_up(self):
        h1 = MaxHeap(4)
        h1.heap = [None,1,2,3]
        h1.num_items = 3
        h1.perc_up(3)
        self.assertEqual(h1.contents(), [3,2,1])
        
    def test_13_heap_sort_ascending(self):
        alist = [7,6,5,4,8,3,2,1]
        h1 = MaxHeap()
        #print(h1.heap_sort_ascending(alist))
    
if __name__ == '__main__':
    unittest.main()