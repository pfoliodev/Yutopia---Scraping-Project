# test_utils.py
import unittest
from utils import string_to_boolean, convert_string_to_int, convert_string_to_float

class TestUtils(unittest.TestCase):

    def test_string_to_boolean_in_stock(self):
        stock_element = type('', (), {'text': 'In stock'})()  # Mock a BeautifulSoup element
        self.assertTrue(string_to_boolean(stock_element))

    def test_string_to_boolean_out_of_stock(self):
        stock_element = type('', (), {'text': 'Out of stock'})()  # Mock a BeautifulSoup element
        self.assertFalse(string_to_boolean(stock_element))

    def test_convert_string_to_int_with_numbers(self):
        self.assertEqual(convert_string_to_int("There are 10 books available."), 10)

    def test_convert_string_to_int_without_numbers(self):
        self.assertEqual(convert_string_to_int("No numbers here."), 0)

    def test_convert_string_to_float_with_float(self):
        self.assertEqual(convert_string_to_float("The price is $12.99."), 12.99)

    def test_convert_string_to_float_with_integer(self):
        self.assertEqual(convert_string_to_float("The quantity is 5."), 5.0)

if __name__ == '__main__':
    unittest.main()
