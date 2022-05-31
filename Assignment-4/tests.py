from concordance import *
from hash_quad import *
import unittest
import filecmp

class Testing(unittest.TestCase):
    
    def test1(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_output.txt")
        self.assertTrue(filecmp.cmp('file1_sol.txt', 'file1_output.txt'))
        
    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_output.txt")
        self.assertTrue(filecmp.cmp('file2_sol.txt', 'file2_output.txt'))
        
    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_output.txt")
        self.assertTrue(filecmp.cmp('declaration_sol.txt', 'declaration_output.txt'))
        
    def test_04(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("test_stop.txt")
        conc.write_concordance("test_stop_output.txt")
        
if __name__ == '__main__':
    unittest.main()
        