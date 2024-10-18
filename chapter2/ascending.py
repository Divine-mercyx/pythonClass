number1 = float(input("enter first float value: "))
number2 = float(input("enter second float value: "))
number3 = float(input("enter third float value"))

numbers = sorted([number1, number2, number3])

for i in numbers:
    print(f"{i}")

