import unittest
from get_multiples import get_multiples

class MyTestCase(unittest.TestCase):

    def test_that_it_returns_correct_input(self):
        actual = get_multiples(1, 10, 2)
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(actual, expected)

    def test_that_get_multiples_raises_exception_with_invalid_input(self):
        with self.assertRaises(ValueError):
            actual = get_multiples(1, -10, 2) 

if __name__ == '__main__':
    unittest.main()
