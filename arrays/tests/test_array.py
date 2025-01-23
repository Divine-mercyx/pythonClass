import unittest
from arrays import array
from arrays.array import MyArray


class MyTestCase(unittest.TestCase):
    def test_that_function_exists(self):
        array = MyArray(10)
        array.put(12)

    def test_the_array_length_fucntion(self):
        array = MyArray(10)
        actual = array.length()
        expected = 10
        self.assertEqual(actual, expected)

    def test_that_the_array_clears_previous_elements(self):
        array = MyArray(4)
        array.put("dog")
        array.put("5")
        array.put("12")
        array.put("12")
        array.clear()
        self.assertEqual(array.length(), 4)
        array.put("boy")
        self.assertEqual(array.length(), 4)

    def test_that_the_array_is_empty(self):
        array = MyArray(4)
        self.assertTrue(array.is_empty())
        array.put("pizza")
        self.assertFalse(array.is_empty())


    def test_that_the_array_equals_another_array(self):
        array = MyArray(4)
        another_array = MyArray(4)
        self.assertTrue(array == another_array)

if __name__ == '__main__':
    unittest.main()
