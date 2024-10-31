number_of_days = int(input("enter number of days: "))

if number_of_days > 0:
    if number_of_days >= 5 and number_of_days < 6:
        print("50 paise")
    elif number_of_days >= 6 and number_of_days <= 10:
        print("1 rupee")
    elif number_of_days > 10 and number_of_days <= 30:
        print("5 rupees")
    elif number_of_days > 30:
        print("membership is cancelled")

else:
    print("invalid input")