first_number = float(input("enter first decimal value: "))
second_number = float(input("enter second decimal value: "))

whole_first_number = int(first_number)
whole_second_number = int(second_number)

result_first_number = first_number - whole_first_number
result_second_number = second_number - whole_second_number

if result_first_number == result_second_number:
    print(f"{result_first_number:.3f} and {result_second_number:.3f} are the same")
else:
    print("they are not the same")