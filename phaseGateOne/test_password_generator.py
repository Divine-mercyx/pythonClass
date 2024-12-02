from unittest import TestCase
from password_generator import *

class TestGetPasswordFunction(TestCase):
    def test_that_get_password_generated_function_exists(self):
        get_password_generated()
        
    def test_that_get_password_generated_returns_correct(self):
        self.assertRaises(TypeError, get_password_generated, None)
