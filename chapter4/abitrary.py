def get_product(*args):
	number = 1
	for value in args:
		number *= value
	return number


print(get_product(12, 45, 67))