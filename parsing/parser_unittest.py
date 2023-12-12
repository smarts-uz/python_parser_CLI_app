#Example of unit testing provided by cluade.ai

import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
from functions import correct_time_data, define_type
from parser import get_info

class TestFunctions(unittest.TestCase):

    def test_correct_time_data(self):
        data = "15.10.2021 10:10:08" 
        expected = "2021-10-15 10:10:08"
        self.assertEqual(correct_time_data(data), expected)

    def test_define_type(self):
        url = "https://example.com"
        self.assertEqual(define_type(url), "url")
        
        text = "some text"
        self.assertEqual(define_type(text), "text")

class TestParser(unittest.TestCase):

    @patch("parser.get_html")
    def test_get_info(self, mock_get_html):
        # Create a mock BeautifulSoup object
        test_html = BeautifulSoup("<html>test</html>", "html.parser")  
        mock_get_html.return_value = test_html
        
        # Call get_info with mock object
        result = get_info(test_html)

        # Assert expected return value
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
