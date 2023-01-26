import unittest
from main import *

class GooseFilterTest(unittest.TestCase):
    def test_goose_filter(self):
        self.assertEqual(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
        self.assertEqual(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]),["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
        self.assertEqual(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]),[])

if __name__ == "__main__":
    unittest.main()
