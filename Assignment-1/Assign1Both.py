# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

def first_string(strlist: list) -> str:
    '''Recursively finds and returns "first" string in a given string list'''
    if strlist == None:
        return None
    elif strlist.rest == None:
        return strlist.value
    else: 
        curr_str = strlist.value
        next = first_string(strlist.rest)
        if next != None and next < curr_str:
            return next
        return curr_str

def split_list(strlist: list):
    '''Return a tuple with 3 lists (nodes) based on first character'''
    vowels = "aeiouAEIOU"
    if strlist == None:
        return None
    else: 
        val = strlist.value

        rec = split_list(strlist.rest)
        if rec == None:
            rec = (None, None, None)
        if val[0] in vowels:
            return Node(val, rec[0]), rec[1], rec[2]
        elif val[0].isalpha() == True:
            return rec[0], Node(val, rec[1]), rec[2]
        else: 
            return rec[0], rec[1], Node(val, rec[2])
        
temp = ["Yellow", ["abc", ["$7.25"]]]
temp = ["Yellow", "abc", "$7.25", "lime", "42", "Ethan"]
print(repr(temp))
print(temp)
mylist = Node("dog", [])
mylist = Node("cat" , mylist)
mylist = Node("fish", mylist)
print(mylist)
print(repr(mylist))
print(str(mylist))



# --------------------------



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
        strlist = Node("B", Node("E", Node("2", Node("C", Node("A", Node("1", None))))))
        self.assertEqual(split_list(strlist),(Node("E", Node("A", None)), Node("B", Node("C", None)), Node("2", Node("1", None))))
       
    def test_split2(self):
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist),(Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))


if __name__ == "__main__":
        unittest.main()
        
        
#------------

def perm_gen_lex(str_in: str) -> list:
    '''Return a list of all possible permutations of input string'''
    if type(str_in) != str:
        print("Error: Wrong input type")
        raise ValueError
    perm = []
    if len(str_in) == 1:
        return [str_in]
    else:
        for idx in range(len(str_in)):
            first = str_in[idx]
            next = str_in[:idx] + str_in[idx + 1:]
            for item in perm_gen_lex(next):
                perm.append(first + item)
    return perm

#---------------

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
