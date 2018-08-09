import unittest
import random
from BinarySearch import binary_search_recursive, binary_search_iterative

class testBinarySearch(unittest.TestCase):
    def setUp(self):
        self.data_1 = [x for x in range(21)]

    def test_binary_search_recursive(self):
        self.assertEqual(binary_search_recursive(self.data_1, 0, self.data_1[0], len(self.data_1) - 1), 0)
        self.assertEqual(binary_search_recursive(self.data_1, 15, self.data_1[0], len(self.data_1) - 1), 15)
        self.assertEqual(binary_search_recursive(self.data_1, 20, self.data_1[0], len(self.data_1) - 1), 20)

    def test_binary_search_iterative(self):
        self.assertEqual(binary_search_iterative(self.data_1, 0, self.data_1[0], len(self.data_1) - 1), 0)
        self.assertEqual(binary_search_iterative(self.data_1, 15, self.data_1[0], len(self.data_1) - 1), 15)
        self.assertEqual(binary_search_iterative(self.data_1, 20, self.data_1[0], len(self.data_1) - 1), 20)

if __name__ == '__main__':
    unittest.main()
