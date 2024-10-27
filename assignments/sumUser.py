choice = 0
first = 0
second = 0

while choice != -1:
    first = int(input("enter the first number: "))
    second = int(input("enter the second number: "))
    sum = first + second
    print(f"sum: {sum}")
    choice = int(input("do you want to continue ? enter 0 to continue or -1 to quit: "))
    if choice == -1:
        print("you've exited the program!")
    