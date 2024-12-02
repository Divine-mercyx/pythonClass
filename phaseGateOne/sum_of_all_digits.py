"""
Psuedocode
-----------------------------------------------
prompt the user to enter a number between 0 and 1000
collect the response
store the response as number
if number is less than zero
return invalid input, number below zero
create a variable total
assign zero to total
while number is greater than zero
number % 10
store the result as remainder
plus remainder to total
divide number by 10
and the result should be assigned to number
"""
def sum_all_digits():
    number = int(input("enter a number between 0 and 1000 to get the sum of all digits: "))
    if number < 0:
        return "invalid input, number below zero"
    total = 0
    while number > 0:
        remainder = number % 10
        total += remainder
        number //= 10
    return total
    
print(sum_all_digits())
