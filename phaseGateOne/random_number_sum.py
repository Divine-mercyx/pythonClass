import random
"""
Psuedocode
--------------------------------------------------
generate a number from 1 to 100
collect the number
store the number as first_number
generate another number from 1 to 100
collect the number
store the number as second_number
add first_number _ second_number
store the result as sum_of_two_number
prompt the user to enter the sum of first_number + second_number
collect the user response
store the response as answer
if answer == sum_of_two_number
display True
else display False
"""
first_number = random.randint(1, 99)
second_number = random.randint(1, 99)

sum_of_two_number = first_number + second_number
answer = int(input(f"enter the sum of  {first_number} + {second_number}: "))
if answer == sum_of_two_number:
    print(True)
else:
    print(False)
