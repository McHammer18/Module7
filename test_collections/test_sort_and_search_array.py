import unittest
from fun_with_collections import sort_and_search_array as array


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.intial_array = array.make_array()
        self.expected_array = [20, 23, 35, 42, 45]


    def test_search_array_found(self):
        self.assertEqual(array.search_array(self.intial_array, 50), 50)


    def test_search_array_not_found(self):
        self.assertEqual(array.search_array(self.intial_array, 36), -1)


if __name__ == '__main__':
    unittest.main()
