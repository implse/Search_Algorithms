import unittest
from Linear_Search import ordered_linear_search, unordered_linear_search

class testLinearSearch(unittest.TestCase):
        def setUp(self):
            self.data_1 = [534, 246, 933, 127, 277, 321, 454, 565, 220]
            self.data_2 = [1, 5, 12, 14, 20, 22, 31, 46, 54]

        def test_unordered_linear_search(self):
            self.assertEqual(unordered_linear_search(self.data_1, 277), 4)
            self.assertEqual(unordered_linear_search(self.data_1, 499), -1)

        def test_ordered_linear_search(self):
            self.assertEqual(ordered_linear_search(self.data_2, 12), 2)
            self.assertEqual(ordered_linear_search(self.data_2, 45), -1)

if __name__ == '__main__':
    unittest.main()
