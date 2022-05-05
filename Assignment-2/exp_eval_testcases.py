import unittest
from exp_eval import * 

class test_expressions(unittest.TestCase):

    def test_invalid(self):
        self.assertFalse(postfix_valid(""))
        self.assertFalse(postfix_valid("2 3"))
        self.assertFalse(postfix_valid("1 + "))
        self.assertFalse(postfix_valid("* 1 2"))
        self.assertFalse(postfix_valid("11"))
        self.assertFalse(postfix_valid("2 3 * /"))
 
    def test_valid(self):
        self.assertTrue(postfix_valid("2.0 3 +"))
        self.assertTrue(postfix_valid("2 -3 -"))
        self.assertTrue(postfix_valid("2 3 *"))
        self.assertTrue(postfix_valid("0.2 -43 /"))
        self.assertTrue(postfix_valid("2 3 4 5 * * *"))
        self.assertTrue(postfix_valid("2 3 4 / ^"))

    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("3 5 -"), -2)
        self.assertAlmostEqual(postfix_eval("3 5 *"), 15)
        self.assertAlmostEqual(postfix_eval("3 5 /"), 0.6)
        self.assertAlmostEqual(postfix_eval("-3 .5 /"), -6)
        self.assertAlmostEqual(postfix_eval("-.1 10.0 *"), -1)
        self.assertAlmostEqual(postfix_eval("2 2 2 ^ ^"), 16)

    def test_inToPostBasicAssoc(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6 - 3 + 5"), "6 3 - 5 +")
        self.assertEqual(infix_to_postfix("6 / 3 + 2"), "6 3 / 2 +")
        self.assertEqual(infix_to_postfix("1 - 2 * 3"), "1 2 3 * -")
        self.assertEqual(infix_to_postfix("6 + 3 / 2"), "6 3 2 / +")
        self.assertEqual(infix_to_postfix("6 + 3 ^ 2"), "6 3 2 ^ +")
        self.assertEqual(infix_to_postfix("6 ^ 3 / 2"), "6 3 ^ 2 /")
        
    def test_inToPostBasicAssoc1(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")
        self.assertEqual(infix_to_postfix("6 - ( ( 3 + 2 ) - 3 )"), "6 3 2 + 3 - -")
        self.assertEqual(infix_to_postfix("6 ^ ( ( 3 - 2 ) / 3 )"), "6 3 2 - 3 / ^")
        self.assertEqual(infix_to_postfix("6 ^ 3 - 2 / 3"), "6 3 ^ 2 3 / -")
        
    def test_inToPostBasicAssoc2(self):
        self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")
        self.assertEqual(infix_to_postfix("6.0 ^ 3.5 ^ -2"), "6.0 3.5 -2 ^ ^")
        self.assertEqual(infix_to_postfix("-6 ^ 0.3 ^ -.2"), "-6 0.3 -.2 ^ ^")

    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")

    def test_inToPostBasicAssoc5(self):
        self.assertEqual(infix_to_postfix("6"), "6")
        with self.assertRaises(ValueError): 
            postfix_eval("3 0 /")

if __name__ == "__main__":
    unittest.main()
