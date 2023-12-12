#Example of unit testing provided by cluade.ai

import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    def test_correct_post_title(self):
        title = "Test Title | Another test #hash" 
        expected = ["Another test", "Test Title"]
        self.assertEqual(correct_post_title(title), expected)

    def test_correct_video_title(self):
        path = r"video_files\my_video.mp4"
        title = ["Video Title"]
        expected = r"\my_video.mp4"
        self.assertEqual(correct_video_title(path, title), expected)

    def test_correct_data_title(self):
        dt = datetime(2023, 2, 15, 13, 55, 10)
        expected = "2023"
        self.assertEqual(correct_data_title(dt), expected)

class TestStructuring(unittest.TestCase):
    
    def test_create_dirs_all(self):
        # Mock data and expected output
        data = [(None, "Channel | Video title", "video_1.mp4", "Desc", "01:20:30", datetime(2023,1,15),)] 
        expected_path = r"path\to\save\Video title"

        # Check if directory is created
        self.assertFalse(os.path.exists(expected_path)) 
        create_dirs_all(data)
        self.assertTrue(os.path.exists(expected_path))

class TestYearConverter(unittest.TestCase):

    def test_correct_time_data(self):
        data = "15.10.2021 10:10:08"
        expected = "2021-10-15 10:10:08"
        self.assertEqual(correct_time_data(data), expected)
    
    def test_year_converter(self):
        data = "2023-02-15 13:55:10" 
        expected = "2023"
        self.assertEqual(year_converter(data), expected)
