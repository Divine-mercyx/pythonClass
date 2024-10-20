print("enter five numbers: ")
number1 = int(input("\n"))
number2 = int(input("\n"))
number3 = int(input("\n"))
number4 = int(input("\n"))
number5 = int(input("\n"))

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0

if number1 < 30 and number2 < 30 and number3 < 30 and number4 < 30 and number5 < 30:
    while counter1 < number1:
        print("*", end = " ")
        counter1 += 1

    print()

    while counter2 < number2:
        print("*", end = " ")
        counter2 += 1

    print()

    while counter3 < number3:
        print("*", end = " ")
        counter3 += 1

    print()

    while counter4 < number4:
        print("*", end = " ")
        counter4 += 1

    print()

    while counter5 < number5:
        print("*", end = " ")
        counter5 += 1
else:
    print("exceeded the limit!")