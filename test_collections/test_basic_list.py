import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as basic
from fun_with_collections import  basic_list_exception


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic.make_list(), [5, 5, 5, 5, 5])


class TestListNonNumeric(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


class TestListBelow(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


class TestListAbove(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


if __name__ == '__main__':
    unittest.main()
