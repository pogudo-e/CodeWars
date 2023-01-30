import unittest
from main import *

class Get_Middle_Test(unittest.TestCase):
    def test_get_middle(self):
        self.assertEqual(get_middle("test"),"es")
        self.assertEqual(get_middle("testing"),"t")
        self.assertEqual(get_middle("middle"),"dd")
        self.assertEqual(get_middle("A"),"A")

if __name__ == "__main__":
    unittest.main()
