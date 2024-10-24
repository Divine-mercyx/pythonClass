number = float(input("enter a number: "))

convert_binary = " "

while number > 0:
    remaining = number % 2
    convert_binary = str(remaining) + convert_binary
    number = number // 2
    

print(convert_binary)