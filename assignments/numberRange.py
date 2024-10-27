start = int(input("enter the start value: "))
stop = int(input("enter the stop value: "))
number_range = int(input("enter the range value: "))
count = 0

while start <= stop:
    if start % 3 == 0:
        count += 1
    start += 1

print(count)   