import unittest
from number_of_characters import *


class TestGetNumberFunction(unittest.TestCase):

    def test_that_function_exists(self):
        get_number_of_characters("")

    def test_that_function_returns_correct_value(self):
        actual = get_number_of_characters("abcdcce")
        expected = {'a': 1, 'b': 1, 'c': 3, 'd': 1, 'e': 1}
        self.assertEqual(actual, expected)

    def test_that_function_doesnt_work_with_integers(self):
        with self.assertRaises(ValueError):
            get_number_of_characters(123)

    def test_that_function_doesnt_work_with_None(self):
        with self.assertRaises(ValueError):
            get_number_of_characters(None)

    def test_that_function_still_works_with_empty_string(self):
        actual = get_number_of_characters("")
        expected = {}
        self.assertEqual(actual, expected)



class TestSwapStringFunction(unittest.TestCase):

    def test_that_funtion_exists(self):
        swap_strings("abc", "xyz")

    def test_that_function_returns_correct_value(self):
        actual = swap_strings("abc", "xyz")
        expected = "xyc abz"
        self.assertEqual(actual, expected)

    def test_that_funtion_works_with_value_length_more_than_three(self):
        actual = swap_strings("abcd", "xyzz")
        expected = "xycd abzz"
        self.assertEqual(actual, expected)

    def test_that_function_doesnt_work_with_integers(self):
        with self.assertRaises(ValueError):
            swap_strings("abc", 1)

    def test_that_function_doesnt_work_with_None(self):
        with self.assertRaises(ValueError):
            swap_strings(None, 1)



class TestPutCeFunction(unittest.TestCase):

    def test_that_function_exists(self):
        put_ce_in_word("hello", "ce")

    def test_that_function_returns_correct_value(self):
        actual = put_ce_in_word("helloo", "ce")
        expected = "helceloo"
        self.assertEqual(actual, expected)
        actual = put_ce_in_word("hello", "ce")
        expected = "helloce"
        self.assertEqual(actual, expected)

    def test_that_function_doesnt_work_with_integers(self):
        with self.assertRaises(ValueError):
            put_ce_in_word("abc", 1)

    def test_that_function_doesnt_work_with_None(self):
        with self.assertRaises(ValueError):
            put_ce_in_word(None, 1)



class TestArrangedFunction(unittest.TestCase):

    def test_that_function_exists(self):
        arrange_word("hello")

    def test_that_function_returns_correct_value(self):
        actual = arrange_word("sEmIColOn")
        expected = "EICOsmoln"
        self.assertEqual(actual, expected)

    def test_that_function_doesnt_work_with_integers(self):
        with self.assertRaises(ValueError):
            arrange_word(12)

    def test_that_function_doesnt_work_with_None(self):
        with self.assertRaises(ValueError):
            arrange_word(None)


class TestNumberOfOccurrencesFunction(unittest.TestCase):

    def test_that_function_exists(self):
        get_number_of_occurence("semicolon", "o")


    def test_that_function_returns_correct_value(self):
        actual = get_number_of_occurence("semicolon", "o")
        expected = ("o", 2)
        self.assertEqual(actual, expected)

    def test_that_function_doesnt_work_with_integers(self):
        with self.assertRaises(ValueError):
            get_number_of_occurence(123, "d")

    def test_that_function_doesnt_work_with_None(self):
        with self.assertRaises(ValueError):
            get_number_of_occurence(None, 1)


class TestRemoveSpecialCharactersFunction(unittest.TestCase):

    def test_that_function_exists(self):
        remove_special_characters("abc")

    def test_that_function_returns_correct_value(self):
        actual = remove_special_characters("a.!b.c")
        expected = "abc"
        self.assertEqual(actual, expected)

    def test_that_function_doesnt_work_with_integers(self):
        with self.assertRaises(ValueError):
            remove_special_characters(123)

    def test_that_function_doesnt_work_with_None(self):
        with self.assertRaises(ValueError):
            remove_special_characters(None)


if __name__ == '__main__':
    unittest.main()
