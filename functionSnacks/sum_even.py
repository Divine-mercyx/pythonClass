def sum_of_even(number):
	sum = 0
	for count in range(0, number + 1, 2):
		sum += count

	return sum


number = int(input("input: "))
print("output: ", sum_of_even(number))