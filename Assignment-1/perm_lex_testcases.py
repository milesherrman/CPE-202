import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        '''Testing empty string'''
        self.assertEqual(perm_lex.perm_gen_lex(''),[])
        '''Testing single letter string'''
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])
        '''Testing two letter string'''
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        '''Testing three letter string'''
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
        '''Testing non-string value'''
        test1 = 15
        with self.assertRaises(ValueError):  
            perm_lex.perm_gen_lex(test1)
        '''Testing None'''
        test2 = None
        with self.assertRaises(ValueError):  
            perm_lex.perm_gen_lex(test2)

if __name__ == "__main__":
        unittest.main()
