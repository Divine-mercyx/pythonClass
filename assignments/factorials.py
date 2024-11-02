number = 5
factorial = 1;
for count in range(1, 6):
    factorial *= (number + 1) - count
    print((number + 1) - count, end = " ")


print()
print(f"factorial: {factorial}")