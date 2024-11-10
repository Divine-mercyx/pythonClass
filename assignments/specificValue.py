def check_specific_value(list):
	value = False
	for number in list:
		if number == 22:
			value = True
	return value



list_of_numbers = [34, 77, 12, 45, 22, 12, 10]
print(check_specific_value(list_of_numbers))
