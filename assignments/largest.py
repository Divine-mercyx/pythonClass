condition = True
largest = 0
smallest = 0

while condition:
    number = int(input("enter a number: "))
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number
    question = int(input("do you want to continue? 1 for(yes) 2 for(no): "))
    if question == 1:
        continue;
    elif question == 2:
        break;
    else:
        print("invalid choice!")

print(f"the largest number is {largest}\nthe smallest number is {smallest}")