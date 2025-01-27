import unittest
from new_array.new_array import NewArray


class TestNewArray(unittest.TestCase):
    def test_length_of_array(self):
        array = NewArray(4)
        self.assertEqual(4, len(array))

    def test_to_put_something_in_the_array(self):
        array = NewArray(4)
        array[0] = 12
        self.assertEqual(12, array[0])

    def test_to_clear_and_check_the_size(self):
        array = NewArray(4)
        array[0] = 12
        self.assertEqual(1, array.get_size())


if __name__ == '__main__':
    unittest.main()
