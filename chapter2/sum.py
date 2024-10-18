number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))
number_3 = int(input("enter third number: "))

sum = number_1 + number_2 + number_3
average = (number_1 + number_2 + number_3) / 3
product = number_1 * number_2 * number_3
smallest_number = number_1
largest = number_1

if number_2 < smallest_number:
    smallest_number = number_2
elif number_3 < smallest_number:
    smallest_number = number_3
elif number_2 > largest:
    largest = number_2
elif number_3 > smallest_number:
    largest = number_3

print(f"sum: {sum}\naverage: {average}\nproduct: {product}\nsmallest number: {smallest_number}\nlargest number: {largest}")