import unittest
from main import *

class SummationTest(unittest.TestCase):
    def test_summation(self):
        self.assertEqual(say_hello('Mr. Spock'), 'Hello, Mr. Spock')
        self.assertEqual(say_hello('Captain Kirk'), 'Hello, Captain Kirk')
        self.assertEqual(say_hello('Liutenant Uhura'), 'Hello, Liutenant Uhura')

if __name__ == "__main__":
    unittest.main()