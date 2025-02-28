import unittest
from sevenSegment.seven_segment import *


class TestSevenSegment(unittest.TestCase):

    def test_segment_function_to_draw_one(self):
        segment = SevenSegment()
        actual = segment.draw_one()
        expected = [
            [" ", " ", " ", "#"],
            [" ", " ", " ", "#"],
            [" ", " ", " ", " "],
            [" ", " ", " ", "#"],
            [" ", " ", " ", "#"]
        ]
        self.assertEqual(actual, expected)


    def test_segment_function_to_draw_two(self):
        segment = SevenSegment()
        actual = segment.draw_two()
        expected = [
            ["#", "#", "#", "#"],
            [" ", " ", " ", "#"],
            ["#", "#", "#", "#"],
            ["#", " ", " ", " "],
            ["#", "#", "#", "#"]
        ]
        self.assertEqual(actual, expected)


    def test_segment_function_to_draw_three(self):
        segment = SevenSegment()
        actual = segment.draw_three()
        expected = [
            ["#", "#", "#", "#"],
            [" ", " ", " ", "#"],
            ["#", "#", "#", "#"],
            [" ", " ", " ", "#"],
            ["#", "#", "#", "#"]
        ]
        self.assertEqual(actual, expected)


    def test_segment_function_to_draw_four(self):
        segment = SevenSegment()
        actual = segment.draw_four()
        expected = [
            ["#", " ", " ", "#"],
            ["#", " ", " ", "#"],
            ["#", "#", "#", "#"],
            [" ", " ", " ", "#"],
            [" ", " ", " ", "#"]
        ]
        self.assertEqual(actual, expected)


    def test_segment_function_to_draw_five(self):
        segment = SevenSegment()
        actual = segment.draw_five()
        expected = [
            ["#", "#", "#", "#"],
            ["#", " ", " ", " "],
            ["#", "#", "#", "#"],
            [" ", " ", " ", "#"],
            ["#", "#", "#", "#"]
        ]
        self.assertEqual(actual, expected)


    def test_segment_function_to_draw_six(self):
        segment = SevenSegment()
        actual = segment.draw_six()
        expected = [
            ["#", "#", "#", "#"],
            ["#", " ", " ", " "],
            ["#", "#", "#", "#"],
            ["#", " ", " ", "#"],
            ["#", "#", "#", "#"]
        ]
        self.assertEqual(expected, actual)


    def test_segment_function_to_draw_seven(self):
        segment = SevenSegment()
        actual = segment.draw_seven()
        expected = [
            ["#", "#", "#", "#"],
            [" ", " ", " ", "#"],
            [" ", " ", " ", "#"],
            [" ", " ", " ", "#"],
            [" ", " ", " ", "#"]
        ]
        self.assertEqual(actual, expected)


    def test_segment_function_to_draw_eight(self):
        segment = SevenSegment()
        actual = segment.draw_eight()
        expected = [
            ["#", "#", "#", "#"],
            ["#", " ", " ", "#"],
            ["#", "#", "#", "#"],
            ["#", " ", " ", "#"],
            ["#", "#", "#", "#"]
        ]
        self.assertEqual(actual, expected)



    def test_segment_function_to_draw_nine(self):
        segment = SevenSegment()
        actual = segment.draw_nine()
        expected = [
            ["#", "#", "#", "#"],
            ["#", " ", " ", "#"],
            ["#", "#", "#", "#"],
            [" ", " ", " ", "#"],
            ["#", "#", "#", "#"]
        ]
        self.assertEqual(actual, expected)