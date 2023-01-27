import unittest
from main import *

class SnailTest(unittest.TestCase):
    def test_snail(self):
        self.assertEqual(snail(3,2,1), 2)
        self.assertEqual(snail(10,3,1), 5)
        self.assertEqual(snail(10,3,2), 8)
        self.assertEqual(snail(100,20,5), 7)

if __name__ == "__main__":
    unittest.main()
