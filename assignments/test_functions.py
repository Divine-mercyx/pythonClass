from unittest import TestCase
from switch_list import *

class TestSwitchListFunction(TestCase):
    def test_that_switch_list_function_exists(self):
        switch_list([1, 2, 3], 2)
        
    def test_that_switch_list_returns_correct_value(self):
        actual = switch_list([1, 2, 3, 4, 5], 2)
        expected = [3, 4, 5, 1, 2]
        self.assertEqual(actual, expected)
        
    def test_that_switch_list_funcction_accepts_None_values(self):
        self.assertRaises(TypeError, switch_list, None)
        
        
        

class TestSplitListFunction(TestCase):
    def test_that_split_array_function_exists(self):
        split_array([1, 2, 3, 4, 5, 6])
        

    def test_that_split_array_returns_correct_value(self):
        actual = split_array([1, 2, 3, 4, 5, 6])
        expected = "[1, 2, 3]  [4, 5, 6]"
        self.assertEqual(actual, expected)
        
        
    def test_that_split_array_funcction_accepts_None_values(self):
        self.assertRaises(TypeError, split_array, None)
        
        
        
        
class TestBooleanListFunction(TestCase):
    def test_that_boolean_list_function_exists(self):
        boolean_list([1, 2, 3, 4, 5])
        
    def test_that_boolean_list_funtion_returns_correct_value(self):
        actual = boolean_list([1, 2, 3, 4, 5, 7])
        expected = [False, True, False, True, False, False]
        self.assertEqual(actual, expected)
