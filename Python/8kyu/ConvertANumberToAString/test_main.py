import unittest
from main import *

class NumberToStringTest(unittest.TestCase):
    def test_number_to_string(self):
        self.assertEqual(number_to_string(67), "67")
        self.assertEqual(number_to_string(789585), "789585")
        self.assertEqual(number_to_string(1+2), '3')


if __name__ == "__main__":
    unittest.main()