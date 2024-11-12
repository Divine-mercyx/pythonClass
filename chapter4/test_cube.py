from unittest import TestCase
import multiplytwonumbers

class testMultiplyFunction(TestCase):
	def test_that_multiply_function_exists(self):
		multiplytwonumbers.multiply(3, 5)


	def test_that_multiply_function_returns_correct_value(self):
		actual = multiplytwonumbers.multiply(2, 2)
		expected = 4
		self.assertEqual(actual, expected)


	def test_that_multiply_function_returns_zero_if_multiplied_by_zero(self):
		actual = multiplytwonumbers.multiply(0, 4)
		expected = 0
		self.assertEqual(actual, expected)


	def test_that_multiply_function_take_negatives_arguments(self):
		self.assertRaises(TypeError, multiplytwonumbers.multiply, -2, -2)


	def test_that_multiply_function_parameter_is_not_empty(self):
		self.assertRaises(ValueError, multiplytwonumbers.multiply, None, None)


	def test_that_multiply_function_one_parameter_is_not_None(self):
		self.assertRaises(ValueError, multiplytwonumbers.multiply, 3, None)


	def test_that_multiply_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, multiplytwonumbers.multiply, "string", "anotherString")


	def test_that_multiply_function_will_accept_first_value_if_float(self):
		actual = multiplytwonumbers.multiply(2.4, 2)
		expected = 4.8
		self.assertEqual(actual, expected)



	def test_that_multiply_function_will_accept_second_value_if_float(self):
		actual = multiplytwonumbers.multiply(2, 2.4)
		expected = 4
		self.assertEqual(actual, expected)



	def test_that_multiply_function_raise_exception_with_double_value(self):
		self.assertRaises(TypeError, multiplytwonumbers.multiply, 2.4, 2.6)







	




