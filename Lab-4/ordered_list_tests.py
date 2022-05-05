import unittest
from ordered_list import *

class TestOrderedList(unittest.TestCase):

    def test_init(self):
        l1 = OrderedList()
        self.assertEqual(l1.head, None)
        self.assertEqual(l1.num_items, 0)
    
    def test_eq(self):
        l1 = OrderedList()
        l1.add(1)
        l2 = OrderedList()
        l2.add(2)
        l3 = OrderedList()
        l3.add(1)
        self.assertNotEqual(l1, l2)
        self.assertNotEqual(l2,l3)
        self.assertEqual(l1,l3)
    
    def test_repr(self):
        l1 = OrderedList() 
        self.assertEqual(l1.__repr__(), "Ordered List: []")
    
    def test_add(self):
        l1 = OrderedList()
        l1.add(10)
        l1.add(20)
        l1.add(30)
        self.assertEqual(l1.get_items(), [10,20,30])
        l1.add(5)
        l1.add(15)
        l1.add(25)
        self.assertEqual(l1.get_items(), [5,10,15,20,25,30])

    def test_remove(self):
        l1 = OrderedList()
        l1.add(10)
        l1.add(20)
        l1.add(30)
        l1.add(40)
        l1.add(50)
        self.assertEqual(l1.get_items(), [10,20,30,40,50])
        l1.remove(10)
        l1.remove(30)
        l1.remove(50)
        self.assertEqual(l1.get_items(), [20,40]) 
        l1.remove(40)
        l1.remove(20)
        self.assertEqual(l1.get_items(), []) 
        
    def test_search_forward(self):
        l1 = OrderedList()
        l1.add(30)
        l1.add(10)
        l1.add(20)
        self.assertTrue(l1.search_forward(10))
        self.assertTrue(l1.search_forward(20))
        self.assertTrue(l1.search_forward(30))
        self.assertFalse(l1.search_forward(5))
        self.assertFalse(l1.search_forward(21))
        self.assertFalse(l1.search_forward(40))
    
    def test_search_backward(self):
        l1 = OrderedList()
        l1.add(2)
        l1.add(4)
        l1.add(6)
        l1.add(8)
        self.assertTrue(l1.search_backward(2))
        self.assertTrue(l1.search_backward(4))
        self.assertTrue(l1.search_backward(6))
        self.assertTrue(l1.search_backward(6))
        self.assertFalse(l1.search_backward(1))
        self.assertFalse(l1.search_backward(3))
        self.assertFalse(l1.search_backward(5))
        self.assertFalse(l1.search_backward(7))
        self.assertFalse(l1.search_backward(9))
        
    def test_size(self):
        l1 = OrderedList()
        self.assertEqual(l1.size(), 0)
        l1.add(2)
        self.assertEqual(l1.size(), 1)
        l1.add(4)
        self.assertEqual(l1.size(), 2)
        l1.remove(2)
        self.assertEqual(l1.size(), 1)
    
    def test_pop(self):
        l1 = OrderedList()
        l1.add(10)
        l1.add(12)
        l1.add(14)
        self.assertEqual(l1.pop(), 14)
        self.assertEqual(l1.pop(), 12)
        self.assertEqual(l1.pop(), 10)
        l1.add(0)
        l1.add(1)
        l1.add(2)
        l1.add(3)
        l1.add(4)
        l1.add(5)
        l1.add(6)
        l1.add(7)
        self.assertEqual(l1.pop(0), 0)
        l1.add(0)
        self.assertEqual(l1.pop(1), 1)
        l1.add(1)
        self.assertEqual(l1.pop(2), 2)
        l1.add(2)
        self.assertEqual(l1.pop(3), 3)
        l1.add(3)
        self.assertEqual(l1.pop(4), 4)
        l1.add(4)
        self.assertEqual(l1.pop(5), 5)
        l1.add(5)
        self.assertEqual(l1.pop(6), 6)
        l1.add(6)
        self.assertEqual(l1.pop(7), 7)
        l1.add(7)
   
        
if __name__ == '__main__': 
    unittest.main()