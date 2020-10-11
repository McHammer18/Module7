import unittest
from fun_with_collections import sort_and_search_array as array


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.initial_array = array.make_array()
        self.expected_array = [20, 23, 35, 42, 45]


    def test_search_array_found(self):
        self.assertEqual(array.search_array(self.initial_array, 50), 50)


    def test_search_array_not_found(self):
        self.assertEqual(array.search_array(self.initial_array, 36), -1)

    def test_sort_inorder(self):
        self.assertEqual(array.sort_array(self.initial_array), self.expected_array)

if __name__ == '__main__':
    unittest.main()
