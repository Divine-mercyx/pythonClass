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


    def test_if_map_contains_a_key(self):
        map = Map()
        self.assertFalse(map.contains_key("1"))
        map.put("1", "i love java")
        self.assertTrue(map.contains_key("1"))


if __name__ == '__main__':
    unittest.main()
