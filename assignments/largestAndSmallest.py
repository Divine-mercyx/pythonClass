number = int(input("enter a number: "))
largest = number
smallest = number

while number != -1:
    number = int(input("enter a number: "))
    if number != -1:
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number

print(largest)
print(smallest)
    