first_income = int(input("enter first persons income: "))
second_income = int(input("enter second person income: "))
third_income = int(input("enter third person income: "))

income_list = [first_income, second_income, third_income]
first_tax_rate = 15 / 100
second_tax_rate = 20 / 100

for i in income_list:
    if i > 0 and i <= 30000:
        rate = i * first_tax_rate
        print(rate)
    elif i > 30000:
        rate = i * second_tax_rate
        print(rate)
