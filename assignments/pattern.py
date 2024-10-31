count = 1
countA = 1
countB = 1

while count <= 13:
    while countA <= 7 - count:
        print(" ", end = " ")
        countA += 1

    while countB <= count:
        print(1, end = " ")
        countB += 1
        print()
    

    count += 1