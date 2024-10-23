largest = 0
count = 1
sum = 0
product = 1

while count <= 3:
    number = int(input("enter a number: "))
    sum += number
    product *= number
    if number > largest:
        largest = number
    count += 1

average = sum / 3
print(f"sum: {sum}\naverage: {average}\nlargest: {largest}\nproduct: {product}")