number = int(input("enter a number: "))

number_one = number % 10
number_two = number // 10
number_three = number_two % 10
number_four = number_two // 10

result = number_four + number_three + number_one
print(result)
