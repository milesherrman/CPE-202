import unittest
from huffman import *

class TestList(unittest.TestCase):
    
    def test_huffman_init(self):
        h1 = HuffmanNode()
        h2 = HuffmanNode(70,2)
        h3 = HuffmanNode(32, 6)
        h1.char_ascii == None
        h1.freq == None
        h2.char_ascii == 70
        h2.freq == 2
        h3.char_ascii == 32
        h3.freq == 6
        
    def test_huffman_eq(self):
        h1 = HuffmanNode(15, 5)
        h2 = HuffmanNode(10, 11)
        h3 = HuffmanNode(15, 5)
        h4 = HuffmanNode(10, 11)
        h1.left = HuffmanNode(15, 5)
        h1.right = HuffmanNode(15, 5)
        h2.left = HuffmanNode(15, 5)
        h4.right = HuffmanNode(15, 5)
        h3.left = HuffmanNode(15, 5)
        h3.right = HuffmanNode(15, 5)    
        self.assertNotEqual(h1, h2)
        self.assertNotEqual(h1, h4)
        self.assertNotEqual(h2, h4)
        self.assertNotEqual(h2, h3)
        self.assertEqual(h1, h3)
    
    def test_comes_before(self):
        h1 = HuffmanNode(60, 1)
        h2 = HuffmanNode(65, 1)
        h3 = HuffmanNode(70, 2)
        h4 = HuffmanNode(75, 2)
        self.assertTrue(comes_before(h1,h2))
        self.assertTrue(h1.__lt__(h2))
        self.assertTrue(comes_before(h3,h4))
        self.assertTrue(h3.__lt__(h4))
        self.assertTrue(comes_before(h1,h3))
        self.assertTrue(h2.__lt__(h4))
        
    def test_cnt_freq(self):
        freqlist1 = cnt_freq("file1.txt")
        anslist1 = [4, 3, 2, 1] 
        self.assertListEqual(freqlist1[97:101], anslist1)
        freqlist2 = cnt_freq("file2.txt")
        anslist2 = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist2[97:104], anslist2)
        freqlist3 = cnt_freq("multiline.txt")
        anslist3 = [3, 0, 0, 0, 5, 2, 0] 
        self.assertListEqual(freqlist3[97:104], anslist3)
        freqlist4 = cnt_freq("singlechar.txt")
        anslist4 = [3, 0, 0, 0, 0, 0, 0] 
        self.assertListEqual(freqlist4[97:104], anslist4)
        #freqlist5 = cnt_freq("empty.txt")
        #anslist5 = [0, 0, 0, 0, 0, 0, 0] 
        #self.assertListEqual(freqlist5[97:104], anslist5)
    
    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char_ascii, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char_ascii, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char_ascii, 100)
    
    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('b')], '001')
        self.assertEqual(codes[ord('c')], '01')
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('f')], '0001')
        
    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
    
    def test_huffman_encode(self):
        #freq = cnt_freq("empty.txt")
        #self.assertEqual(create_huff_tree(freq), None)
        freq = cnt_freq("singlechar.txt")
        self.assertEqual(create_huff_tree(freq), HuffmanNode(97,3))
        
    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        self.assertTrue(compare_files("file1_out.txt", "file1_soln.txt"))
    
    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        self.assertTrue(compare_files("file2_out.txt", "file2_soln.txt"))
    
    def test_03_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        self.assertTrue(compare_files("multiline_out.txt", "multiline_soln.txt"))
    
    def test_04_textfile(self):
        huffman_encode("singlechar.txt", "singlechar_out.txt")
    
   #def test_06_textfile(self):
   #     huffman_encode("empty.txt", "empty_out.txt")
   #     self.assertTrue(compare_files("empty.txt", "empty_out.txt"))
    
def compare_files(file1,file2):
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match

if __name__ == '__main__': 
   unittest.main()