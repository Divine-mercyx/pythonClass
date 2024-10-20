condition = True


while condition:
    number1 = int(input("enter first number: "))
    number2 = int(input("enter second number: "))
    print(number1 + number2)
    question = int(input("do you want to do the operation again? 1 for(yes) 2 for(no) "))
    if question == 1:
        condition = True
    elif question == 2:
        condition = False
        print("program terminated")
    else:
        print(f"{question} is a invalid choice!")
        condition = False