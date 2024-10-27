value = input("enter a value: ")

if len(value) == 1:
    if value.isalpha():
        if value.lower() in ("a", "e", "i" "o", "u"):
            print(f"{value} is a vowel")
        else:
            print(f"{value} is a consonant")
    else:
        print(f"{value} is a number")
else:
    print("input length more than one")