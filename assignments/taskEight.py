
count = 1
countB = 1
multiple = 1
multipleB = 1
countC = 1
sumA = 0
sumB = 0

while count <= 10:
    if count % 4 == 0:
        if count / 4 == 1:
            while countB <= 5:
                multiple = multiple * count
                sumA += multiple
                countB += 1

        elif count / 4 == 2:
            while countC <= 5:
                multipleB = multipleB * count
                sumB += multipleB
                countC += 1

    count += 1


else:
    overall = sumA + sumB
    print(overall)