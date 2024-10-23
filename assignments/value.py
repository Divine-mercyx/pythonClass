positive = 0
negative = 0
zero = 0
count = 1

while count <= 5:
    number = float(input("enter a number: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1
    count += 1

print(f"positive count: {positive}\nnegative count: {negative}\nzero count: {zero}")