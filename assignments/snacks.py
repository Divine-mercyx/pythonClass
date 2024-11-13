import math

def get_division_or_square(number):
    if number is None:
        raise ValueError
        
    if type(number) is int:
        if number > 0:
            if number % 5 == 0:
                return round(math.sqrt(number), 2)
            else:
                return int(number / 5)
    raise TypeError



def get_future_investment_value(investment_amount, monthly_interest_rate, years):
    if investment_amount is None \
    or monthly_interest_rate is None \
    or years is None:
        raise TypeError
        
    if type(investment_amount) in [int, float] \
    and type(monthly_interest_rate) in [int, float] \
    and type(years) is int:
        if investment_amount > 0 and monthly_interest_rate > 0 and years > 0:
            number_in_months = years * 12
            monthly_interest_rate = monthly_interest_rate / 100
            future_investment_rate = investment_amount * (1 + monthly_interest_rate) ** number_in_months
            return round(future_investment_rate, 2)
    raise TypeError
    
    
    
def check_float_numbers(first, second):
    if type(first) is not float and type(second) is not float:
        raise TypeError
    if first < 0 or second < 0:
        raise ValueError
    if type(first) is float and type(second) is float:
        return 2
    elif type(first) is float or type(second) is float:
        return 1
        
        

def my_discount(price, discount):
    if price is None or discount is None:
        raise ValueError
    if price > 0 and discount > 0:
        if type(price) in [int, float] and type(discount) in [int, float]:
            discount = discount / 100
            return price - (price * discount)
        raise  TypeError
    raise ValueError
