digits = int(input("enter 5 digit integer: "))
first_number = digits // 10000;
remaining_1 = digits % 10000
second_number = remaining_1 // 1000
remaining_2 = remaining_1 % 1000
third_number = remaining_2 // 100
remaining_3 = remaining_2 % 100
fourth_number = remaining_3 // 10
fifth_number = remaining_3 % 10

print(f"{first_number}   {second_number}   {third_number}   {fourth_number}   {fifth_number}")
