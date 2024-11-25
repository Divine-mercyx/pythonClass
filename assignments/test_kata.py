from unittest import TestCase
from kata import *

class TestForLargestFunction(TestCase):
    def test_that_get_largest_function_exists(self):
        get_largest([2, 3])
        
    def test_that_function_returns_correct_value(self):
        actual = get_largest([1, 2, 3, 4, 5])
        expected = 5
        self.assertEqual(actual, expected)
        
    def test_that_get_largest_function_is_not_empty(self):
        self.assertRaises(TypeError, get_largest, None)
        
        
class TestReverseListFunction(TestCase):
    def test_that_reverse_list_function_exists(self):
        reverse_a_list([2, 3])
        
    def test_that_reverse_a_list_function_returns_correct_value(self):
        actual = reverse_a_list([1, 2, 3, 4, 5])
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)
        
    def test_that_reverse_a_list_function_is_not_empty(self):
        self.assertRaises(TypeError, reverse_a_list, None)
        
        
        

class TestForOccurenceFunction(TestCase):
    def test_that_check_occurance_function_exists(self):
        check_occurance([2, 3], 2)
        
    def test_that_check_occurance_function_returns_correct_value(self):
        actual = check_occurance([1, 2, 3, 4, 5], 2)
        expected = True
        self.assertEqual(actual, expected)
        
    def test_that_check_occurance_function_is_not_empty(self):
        self.assertRaises(TypeError, check_occurance, None)
        
        
class TestReverseListFunction(TestCase):
    def test_that_rprint_odd_numbers_function_exists(self):
        print_odd_numbers([2, 3])
        
    def test_that_print_odd_numbers_function_is_not_empty(self):
        self.assertRaises(TypeError, print_odd_numbers, None)
        





class TestEvenNUmbersFunction(TestCase):
    def test_that_print_even_numbers_function_exists(self):
        print_even_numbers([2, 3])
        
    def test_that_print_even_numbers_function_is_not_empty(self):
        self.assertRaises(TypeError, print_even_numbers, None)
        
        
class TestTotalFunction(TestCase):
    def test_that_reverse_list_function_exists(self):
        get_total([2, 3])
        
    def test_that_reverse_a_list_function_returns_correct_value(self):
        actual = get_total([1, 2, 3])
        expected = 6
        self.assertEqual(actual, expected)
        
    def test_that_reverse_a_list_function_is_not_empty(self):
        self.assertRaises(TypeError, get_total, None)



class TestIsPalindromeFunction(TestCase):
    def test_that_isPalindrome_function_exists(self):
        isPalindrome("madam")
        
    def test_that_isPalindrome_function_returns_correct_value(self):
        actual = isPalindrome("madam")
        expected = True
        self.assertEqual(actual, expected)
        
    def test_that_isPalindrome_function_is_not_empty(self):
        self.assertRaises(TypeError, isPalindrome, None)
        
        
        

class TestGetSumOfNumbersListFunction(TestCase):
    def test_that_get_sum_of_numbers_list_function_exists(self):
        get_sum_of_numbers_list([1, 2, 3])
        
    def test_that_get_sum_of_numbers_list_function_returns_correct_value(self):
        actual = get_sum_of_numbers_list([1, 2])
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_that_get_sum_of_numbers_list_function_is_not_empty(self):
        self.assertRaises(TypeError, get_sum_of_numbers_list, None)
        
        
        
        


class TestJoinListFunction(TestCase):
    def test_that_join_lists_function_exists(self):
        join_lists(["a"], [1, 2, 3])
        
    def test_that_join_lists_function_returns_correct_value(self):
        actual = join_lists(["a", "b"], [1, 2])
        expected = ["a", "b", 1, 2]
        self.assertEqual(actual, expected)
        
    def test_that_join_lists_function_is_not_empty(self):
        self.assertRaises(TypeError, join_lists, None)
        
        
        

class TestJoinListFunction(TestCase):
    def test_that_take_elements_function_exists(self):
        take_elements(["a"], [1, 2, 3])
        
    def test_that_jtake_elements_function_returns_correct_value(self):
        actual = take_elements(["a", "b"], [1, 2])
        expected = ["a", 1, "b", 2]
        self.assertEqual(actual, expected)
        
    def test_that_jtake_elements_function_is_not_empty(self):
        self.assertRaises(TypeError, take_elements, None)
