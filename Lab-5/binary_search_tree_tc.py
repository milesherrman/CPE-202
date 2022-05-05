import unittest
from binary_search_tree import *

class TestBinarySearch(unittest.TestCase):
    def test_init(self):
        t1 = BinarySearchTree()
        self.assertEqual(t1.__repr__(), "Tree with 0 nodes")
    
    def test_eq(self):
        n1 = TreeNode(5)
        n2 = TreeNode(10)
        n3 = TreeNode(5)
        self.assertNotEqual(n1, n2)
        self.assertNotEqual(n2, n3)
        self.assertEqual(n1, n3)
        
    def test_child(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        c1 = t1.root.left
        c2 = t1.root.right
        self.assertTrue(c1.is_left_child())
        self.assertFalse(c1.is_right_child())
        self.assertFalse(c2.is_left_child())
        self.assertTrue(c2.is_right_child())
        
    def test_find_node(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        self.assertEqual(t1.root.find_node(15), TreeNode(15))
        self.assertEqual(t1.root.find_node(5), TreeNode(5))
        self.assertEqual(t1.root.find_node(25), TreeNode(25))
        self.assertEqual(t1.root.find_node(20), TreeNode(20))
    
    def test_insert(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        t1.insert(35)
        self.assertEqual(t1.size, 7)
        self.assertEqual(t1.root.key, 20)
        self.assertEqual(t1.root.left.key, 10)
        self.assertEqual(t1.root.right.key, 30)
        c1 = t1.root.left
        c2 = t1.root.right
        self.assertEqual(c1.parent.key, 20)
        self.assertEqual(c2.parent.key, 20)
        c3 = c1.left
        c4 = c1.right
        c5 = c2.left
        c6 = c2.right
        self.assertEqual(c3.parent.key, 10)
        self.assertEqual(c4.parent.key, 10)
        self.assertEqual(c5.parent.key, 30)
        self.assertEqual(c6.parent.key, 30)
        
    def test_delete(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        t1.insert(1)
        t1.insert(12)
        t1.insert(26)
        t1.insert(40)
        
        t1.delete(5)
        self.assertEqual(t1.root.left.left.key, 1)
        self.assertEqual(t1.root.left.left.parent.key, 10)
        self.assertEqual(t1.root.left.left.level, 2)
        t1.delete(15)
        self.assertEqual(t1.root.left.right.key, 12)
        self.assertEqual(t1.root.left.right.parent.key, 10)
        self.assertEqual(t1.root.left.right.level, 2)
        t1.delete(25)
        self.assertEqual(t1.root.right.left.key, 26)
        self.assertEqual(t1.root.right.left.parent.key, 30)
        self.assertEqual(t1.root.right.left.level, 2)
        t1.delete(35)
        self.assertEqual(t1.root.right.right.key, 40)
        self.assertEqual(t1.root.right.right.parent.key, 30)
        self.assertEqual(t1.root.right.right.level, 2)
        
        t2 = BinarySearchTree()
        t2.insert(20)
        t2.insert(10)
        t2.insert(30)
        t2.insert(5)
        t2.insert(15)
        t2.insert(25)
        t2.insert(35)
        t2.insert(1)
        t2.insert(12)
        t2.insert(26)
        t2.insert(40)
        
        t2.delete(10)
        self.assertEqual(t2.root.left.key, 12)
        self.assertEqual(t2.root.left.right.key, 15)
        self.assertEqual(t2.root.left.right.left, None)
        self.assertEqual(t2.root.left.level, 1)
        
        t2.delete(30)
        self.assertEqual(t2.root.right.key, 35)
        self.assertEqual(t2.root.right.right.key, 40)
        self.assertEqual(t2.root.right.right.level, 2)
        
    def test_find_min(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        c1 = t1.root.left
        c2 = t1.root.right
        self.assertEqual(t1.root.find_min(), 5)
        self.assertEqual(c1.find_min(), 5)
        self.assertEqual(c2.find_min(), 25)
        
    def test_find_max(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        c1 = t1.root.left
        c2 = t1.root.right
        self.assertEqual(t1.root.find_max(), 35)
        self.assertEqual(c1.find_max(), 15)
        self.assertEqual(c2.find_max(), 35)
        
    def test_find_successor(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        c1 = t1.root.left
        c2 = t1.root.right
        self.assertEqual(t1.root.find_successor(), TreeNode(25))
        self.assertEqual(c1.find_successor(), TreeNode(15))
        self.assertEqual(c2.find_successor(), TreeNode(35))
    
    def test_inorder_print_tree(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        #t1.root.inorder_print_tree()
        #print("")
    
    def test_print_levels(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        #t1.root.print_levels()
        #print("")
    
    def test_find(self):
        t1 = BinarySearchTree()
        t1.insert(20)
        t1.insert(10)
        t1.insert(30)
        t1.insert(5)
        t1.insert(15)
        t1.insert(25)
        t1.insert(35)
        self.assertTrue(t1.find(5))
        self.assertTrue(t1.find(35))
        self.assertTrue(t1.find(25))
        self.assertTrue(t1.find(15))
        self.assertFalse(t1.find(125))
        self.assertFalse(t1.find(0))
        self.assertFalse(t1.find(17))
        self.assertFalse(t1.find(21))

if __name__ == '__main__': 
    unittest.main()