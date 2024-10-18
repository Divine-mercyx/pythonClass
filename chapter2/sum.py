number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))
number_3 = int(input("enter third number: "))

sum = number_1 + number_2 + number_3
average = sum / 3
product = number_1 * number_2 * number_3
smallest = min(number_1, number_2, number_3)
largest = max(number_1, number_2, number_3)

print(f"sum: {sum}\naverage: {average}\nproduct: {product}\nsmallest number: {smallest}\nlargest number: {largest}")