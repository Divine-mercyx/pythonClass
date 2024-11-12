def multiply(first, second):
	result = 0
	if first is None or second is None:
		raise ValueError

	if type(first) is int or type(second) is int:
		if first >= 0 and second >= 0:
			for count in range(1, int(second) + 1):
				result = first + result

			return result

		raise TypeError

	raise TypeError


#print(multiply(-2, 3))
