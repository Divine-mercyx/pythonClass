def get_cube(number):
	if type(number) is int:
		return number ** 3
	raise TypeError