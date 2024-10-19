principal_amount = float(input("enter the principal amount: "))
annual_interest_rate = float(input("enter the annual interest rate: "))
duration_in_years = int(input("enter the duration in years: "))

monthly_interest_rate = (annual_interest_rate / 100) / 12
month_duration = duration_in_years * 12
monthly_payment = principal_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** month_duration) / (((1 + monthly_interest_rate) ** month_duration) - 1)
 

print(f"{monthly_payment:.2f}")