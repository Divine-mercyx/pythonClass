import unittest
from arrays.maps.map import Map


class MyTestCase(unittest.TestCase):

    def test_map_size(self):
        map = Map()
        map.put("1", "i love java")
        self.assertEqual(1, map.get_size())


    def test_map_add_text_and_get_it(self):
        map = Map()
        map.put("1", "i love java")
        self.assertEqual(map.get("1"), "i love java")


if __name__ == '__main__':
    unittest.main()
