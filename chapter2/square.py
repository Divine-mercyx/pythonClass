counter = 0

print("numbers\t\tquares\t\tcubes")

while counter <= 5:
    square = counter * counter
    cube = counter * counter * counter
    print(f"{counter}\t\t{square}\t\t{cube}")
    counter += 1;