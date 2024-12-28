
def get_compound_interest(initial_investment, monthly_contribution, length_of_time_in_years, estimated_interest_rate, compound_frequency):
    compound_interest = initial_investment * (1 + estimated_interest_rate / compound_frequency) ** (compound_frequency * length_of_time_in_years) + monthly_contribution * (((1 + estimated_interest_rate / compound_frequency) ** (compound_frequency * length_of_time_in_years) - 1) / (estimated_interest_rate / compound_frequency))
    return compound_interest


def ask_for_details():
    while True:
        try:
            initial_investment = float(input("enter initial investment: "))
            monthly_contribution = float(input("enter monthly contribution: "))
            length_of_time_in_years = int(input("enter length of time in years: "))
            estimated_interest_rate = float(input("enter estimated interest rate: ")) / 100
            interest_rate_variance_range = int(input("enter interest rate variance range: ")) / 100
            compound_frequency = int(input("enter compound frequency: "))
            break
        except ValueError:
            print("enter the correct numeric value")

    compound_interest = get_compound_interest(initial_investment, monthly_contribution, length_of_time_in_years, estimated_interest_rate, compound_frequency)
    print(compound_interest)




ask_for_details()
