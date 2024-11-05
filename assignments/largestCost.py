number = int(input("enter a number: "))
largest = number

counter = 1

while counter < 10:
    number = int(input("enter a number: "))
    if number > largest:
        largest = number
    counter += 1


print(f"{largest}")