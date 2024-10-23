number = int(input("enter a three digit number: "))

number_1 = number // 100
remaining_one = number % 100
number_2 = remaining_one // 10
number_3 = remaining_one % 10

if number_1 == number_3:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")