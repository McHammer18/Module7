import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as basic


class TestList(unittest.TestCase):
    @patch('fun_with_collections.topic1.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic.make_list(), [5, 5, 5])

if __name__ == '__main__':
    unittest.main()
