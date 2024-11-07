def sum_multiples(x, y):
	sum = 0
	for count in range(x, y + 1):
		if count % x == 0:
			sum += count
	return sum


numberX = int(input("enter x: "))
numberY = int(input("enter y: "))

print("output: ", sum_multiples(numberX, numberY))  