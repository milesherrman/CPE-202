# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

class TestLab1(unittest.TestCase):


    def test_max_list_iter(self):

        list1 = [3,1,5,5,2]
        list2 = [9,2,1,0,-5,10]
        list3 = []

        # Testing incorrect parameter type
        tlist = None
        with self.assertRaises(ValueError): 
            max_list_iter(tlist)
        # Testing correct functionality
        self.assertEqual(max_list_iter(list1), 5)
        # Testing correct functionality
        self.assertEqual(max_list_iter(list2), 10)
        # Testing empty list
        self.assertEqual(max_list_iter(list3), None)
        
    def test_reverse_rec(self):
        # Testing correct functionality
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        # Testing correct functionality
        self.assertEqual(reverse_rec([4,7,9,3,1]),[1,3,9,7,4])
        # Testing correct functionality
        self.assertEqual(reverse_rec([11,22,33,99,88,77]),[77,88,99,33,22,11])
        # Testing empty list
        self.assertEqual(reverse_rec([]),[])
        # Testing incorrect parameter type
        tlist = None
        with self.assertRaises(ValueError):  
            reverse_rec(tlist)

    def test_bin_search(self):
    
        # Testing correct functionality
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        # Testing correct functionality
        list_val =[0,1,2,3,4,5,6,7,8]
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 )
        # Testing absent value (out of range on high side)
        list_val =[0,1,2,3,4,5,6,7,8]
        self.assertEqual(bin_search(15, 0, len(list_val)-1, list_val), None )
        # Testing absent value (out of range on low side)
        list_val =[0,1,2,3,4,5,6,7,8]
        self.assertEqual(bin_search(-15, 0, len(list_val)-1, list_val), None )
        # Testing absent value
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )
        # Testing empty list
        list_val = []
        self.assertEqual(bin_search(4, 0, 10, list_val), None )
        # Testing incorrect parameter type
        list_val = None
        with self.assertRaises(ValueError):  
            bin_search(10, 0, 10, list_val)

if __name__ == "__main__":
        unittest.main()
