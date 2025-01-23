import unittest
from functionSnacks import encrypt

class TestEncryptFunction(unittest.TestCase):
    def test_that_function_exist(self):
        encrypt.encrypt_text("happy")

    def test_that_function_returns_correct_value(self):
        actual = encrypt.encrypt_text("a")
        expected = "n"
        self.assertEqual(actual, expected)
        actual = encrypt.encrypt_text("Hello, World")
        expected = "Uryyb, Jbeyq"
        self.assertEqual(actual, expected)

    def test_that_function_throws_type_error(self):
        self.assertRaises(TypeError, encrypt.encrypt_text, 1)
        self.assertRaises(TypeError, encrypt.encrypt_text, None)


    def test_that_function_will_work_for_empty_spaces(self):
        actual = encrypt.encrypt_text("")
        expected = ""
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
