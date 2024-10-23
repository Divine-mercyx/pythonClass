count = 10
duration = 0
duration_month = 0

while count <= 30:
    principal = float(input("enter the principal: "))
    annual_rate = 7 / 100
    duration = count
    annual_interest = principal * ((1 + annual_rate) ** duration)
    print(f"the interest for {count} years is: {annual_interest}")
    count += 10