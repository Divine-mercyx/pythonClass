def largest(list):
	largest = list[0]
	for number in list:
		if number > largest:
			largest = number
	return largest


def smallest(list):
	smallest = list[0]
	for number in list:
		if number < smallest:
			smallest = number
	return smallest




list_of_numbers = [34, 77, 12, 45, 22, 12, 10]
print(largest(list_of_numbers))
print(smallest(list_of_numbers))