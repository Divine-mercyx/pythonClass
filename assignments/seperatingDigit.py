number = input("enter a five digit number: ")
space = " "
if number.isdigit():
    for i in number:
        print(i, end = " ")
else:
    print("not a numerical value")