import math

import unittest
from raftel.raftel import _rad_to_degree

class TestRaftel(unittest.TestCase):

    def test_rad_conversion(self):
        self.assertEqual(_rad_to_degree(0), 0)
        self.assertEqual(_rad_to_degree(math.pi), 180)
        self.assertEqual(_rad_to_degree(2*math.pi), 360)

if __name__ == '__main__':
    unittest.main(verbosity=2)
