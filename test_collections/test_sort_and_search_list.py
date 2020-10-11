import unittest
from fun_with_collections import sort_and_search_list as sort_search

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.intial_list = sort_search.make_list()

    def test_sort_inorder(self):
        self.assertEqual(True, False)

    def test_search_found(self):
        self.assertEqual(sort_search.search_list(self.intial_list, 50), 50)


    def test_search_not_found(self):
        self.assertFalse(sort_search.search_list(self.intial_list, 45), 'None')


if __name__ == '__main__':
    unittest.main()
