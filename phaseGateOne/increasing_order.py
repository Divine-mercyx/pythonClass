"""
Pseudocode
-------------------------------------------------------------
prompt the user to enter first number
collect and store the number as first_number
prompt the user to enter second number
collect and store the number as second_number
prompt the user to enter third number
collect and store the number as third_number
create a list that has the value of first_number, second_number, third_number
store the list as list_of_number
display list_of_number index 0, list_of_number index 1, list_of_number index 2
"""


first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
third_number = int(input("enter third number: "))
list_of_number = [first_number, second_number, third_number]
list_of_number.sort()
print(f"{list_of_number[0]}, {list_of_number[1]}, {list_of_number[2]}")
