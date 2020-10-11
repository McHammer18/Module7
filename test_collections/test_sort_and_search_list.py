import unittest
from fun_with_collections import sort_and_search_list as sort_search

class MyTestCase(unittest.TestCase):
    def test_sort_inorder(self):
        self.assertEqual(True, False)


    def test_search_found(self):
        self.assertEqual(50, sort_search.search_list(50))


    def test_search_not_found(self):
        self.assertFalse(50, sort_search.search_list(50))


if __name__ == '__main__':
    unittest.main()
