import unittest
from stacks.stack import Stack


class MyTestCase(unittest.TestCase):
    def test_to_create_stack(self):
        stack = Stack(4)

    def test_to_add_to_stack(self):
        stack = Stack(4)
        stack.push("boy")
        self.assertEqual(4, stack.get_size())

    def test_to_add_item_and_peek_item(self):
        stack = Stack(4)
        stack.push("boy")
        stack.push("girl")
        self.assertEqual("girl", stack.peek())


    def test_to_add_item_then_pop_item(self):
        stack = Stack(4)
        stack.push("boy")
        stack.push("girl")
        self.assertEqual("girl", stack.pop())

if __name__ == '__main__':
    unittest.main()
