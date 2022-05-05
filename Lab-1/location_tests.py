# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    # Purpose: Test Location initialization function
    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc2.name, "Paris")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc2.lat, 48.9)
        self.assertEqual(loc.lon, -120.7)
        self.assertEqual(loc2.lon, 2.4)

    # Purpose: Test Location repr function
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2),"Location('Paris', 48.9, 2.4)")
    
    # Purpose: Test Location eq function
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("Paris", 48.9, 2.4) 
        self.assertNotEqual(loc, loc2)
        self.assertNotEqual(loc, loc3)
        self.assertEqual(loc2, loc3)

if __name__ == "__main__":
        unittest.main()
