"""
pseudocode
----------------------------------------------------------------
create a function called decide_day
that decides the day based on a number
if 1 return monday
if 2 return tuesday
if 3 return wednesday
if 4 return thursday
if 5 return friday
if 6 return saturday
else if 0 return sunday

create another function called get_the_day_number
promept the user to enter today number
collect the number and store it as day_number
prompt the user to enter the number of days elapsed since
collect the number and store it as future_number
create a variaable store the variable as total
assign future_number + day_number result to total
if total < 7 and total >= 0
    call the decide_number function and pass total for it to decide the day
    store the day in future_day
    call the decide_number function and pass total for it to decide the day
    store the day as today
    display today is today and th future day is future_day
else:
    total % 7
    store the result in total
    call the decide_number function and pass total for it to decide the day
    store the day in future_day
    call the decide_number function and pass total for it to decide the day
    store the day as today
    display today is today and th future day is future_day
"""
def get_the_day_number():
    day_number = int(input("enter today number: "))
    future_number = int(input("enter number of days elapsed since: "))
    total = day_number + future_number
    if total < 7 and total >= 0:
        future_day = decide_day(total)
        today = decide_day(day_number)
        print(f"today is {today} and the future day is {future_day}")
    else:
        total = total % 7
        future = decide_day(total)
        today = decide_day(day_number)
        print(f"today is {today} and the future day is {future}")


def decide_day(number):
    if number == 1:
        return "monday"
    elif number == 2:
        return "tuesday"
    elif number == 3:
        return "wednesday"
    elif number == 4:
        return "thursday"
    elif number == 5:
        return "friday"
    elif number == 6:
        return "saturday"
    else:
        return "sunday"

get_the_day_number()
