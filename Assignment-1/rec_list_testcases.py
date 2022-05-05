import unittest
from  rec_list import *

class TestRecList(unittest.TestCase):

    def test_first1(self):
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"49ers")
        strlist = Node("xyz", Node("49ers", Node("Abc", None)))
        self.assertEqual(first_string(strlist),"49ers")

    def test_split1(self):
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))
        #strlist = Node("B", Node("E", Node("2", Node("C", Node("A", Node("1", None))))))
        #self.assertEqual(split_list(strlist),(Node("E", Node("A", None)), Node("B", Node("C", None)), Node("2", Node("1", None))))
       
 #def test_split2(self):
        #strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        #self.assertEqual(split_list(strlist),(Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))


if __name__ == "__main__":
        unittest.main()