import unittest
from sep_chain_ht import *

class TestList(unittest.TestCase):

   def test_insert1(self):
      hash1 = MyHashTable()
      hash1.insert(11, "a") 
      hash1.insert(3, "b")
      self.assertEqual(hash1.size(), 2)
      with self.assertRaises(ValueError):
         hash1.insert(-5, "c")
      with self.assertRaises(ValueError):
         hash1.insert(-15, "c")
      with self.assertRaises(ValueError):
         hash1.insert("l", "c")
      with self.assertRaises(ValueError):
         hash1.insert([87], "c")
      with self.assertRaises(ValueError):
         hash1.insert(8.9, "c")
         
   def test_insert2(self):
      hash1 = MyHashTable()
      hash1.insert(3, "a")
      hash1.insert(14, "b") 
      hash1.insert(25, "c")  
      self.assertEqual(hash1.size(), 3)
      
   def test_rehash1(self):
      hash1 = MyHashTable(3)
      hash1.insert(0, "a")
      hash1.insert(1, "b") 
      hash1.insert(2, "c")
      hash1.insert(3, "d")
      self.assertEqual(hash1.get_item(3), 'd')
      hash1.insert(4, "e")
      self.assertEqual(hash1.get_item(3), 'd')
      self.assertEqual(hash1.size(), 5)
      self.assertEqual(hash1.table_size, 7)
     
   def test_get1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      self.assertEqual(hash1.get_item(3), 'b')
      self.assertEqual(hash1.get_item(11), 'a')
      self.assertEqual(hash1.get_item(1), 'c')
      self.assertEqual(hash1.get_item(8), 'd')
      with self.assertRaises(LookupError):
            hash1.get_item(2)
      with self.assertRaises(LookupError):
            hash1.get_item(4)
      with self.assertRaises(LookupError):
            hash1.get_item(6)
      with self.assertRaises(LookupError):
            hash1.get_item(0)
      
   '''def test_get2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      with self.assertRaises(LookupError):
            hash1.get_item(6)'''

   def test_remove1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      self.assertEqual(hash1.remove(11), (11, 'a'))
      self.assertEqual(hash1.size(), 0)
   
   def test_remove2(self):
      hash1 = MyHashTable(3)
      hash1.insert(0, "a")
      hash1.insert(1, "b") 
      hash1.insert(2, "c")
      hash1.insert(3, "d")
      hash1.insert(4, "e")
      self.assertEqual(hash1.remove(0), (0, 'a'))
      self.assertEqual(hash1.remove(1), (1, 'b'))
      self.assertEqual(hash1.remove(2), (2, 'c'))
      self.assertEqual(hash1.remove(3), (3, 'd'))
      self.assertEqual(hash1.remove(4), (4, 'e'))
      self.assertEqual(hash1.size(), 0)

   def test_load_factor1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      self.assertEqual(hash1.load_factor(), 1.4)
      
   def test_load_factor2(self):
      hash1 = MyHashTable(3)
      hash1.insert(0, "a")
      hash1.insert(1, "b") 
      hash1.insert(2, "c") 
      hash1.insert(0, "d")
      hash1.insert(1, "e") 
      hash1.insert(2, "f") 
      self.assertEqual(hash1.load_factor(), 1)

   def test_collisions2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a") 
      hash1.insert(3, "b") 
      hash1.insert(1, "c") 
      hash1.insert(8, "d") 
      hash1.insert(4, "e") 
      hash1.insert(5, "f") 
      hash1.insert(1, "g") 
      hash1.insert(2, "h")
      self.assertEqual(hash1.collisions(), 2)

if __name__ == '__main__': 
   unittest.main()


