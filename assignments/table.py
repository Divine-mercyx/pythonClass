a = 1
b = 0
power = 0
print("a\tb\tpow(a, b)")

while a <= 5:
    b = a + 1
    power = a ** b
    print(f"{a}\t{b}\t{power}")
    a += 1