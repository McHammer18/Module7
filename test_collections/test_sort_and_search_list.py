import unittest
from fun_with_collections import sort_and_search_list as sort_search


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.intial_list = sort_search.make_list()
        self.expected_list = [20, 23, 35, 42, 45]

    def test_sort_inorder(self):
        self.assertEqual(sort_search.sort_list(self.intial_list), self.expected_list)

    def test_search_found(self):
        self.assertEqual(sort_search.search_list(self.intial_list, 50), 50)


    def test_search_not_found(self):
        self.assertEqual(sort_search.search_list(self.intial_list, 45), -1)


if __name__ == '__main__':
    unittest.main()
