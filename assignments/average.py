list_of_numbers = [34, 77, 12, 45, 22, 12, 10]
sum = 0

for number in list_of_numbers:
	sum += number
average = sum / len(list_of_numbers)
print(f" the average is {average:.2f}")