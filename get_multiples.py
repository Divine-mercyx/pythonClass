def get_multiples(starting_range, ending_range, divisor):
    if starting_range < 0 or ending_range < 0: raise ValueError("invalid range")
    my_arr = []
    while starting_range < (ending_range + 1):
        if starting_range % divisor == 0:
            my_arr.append(starting_range)

        starting_range += 1
    return my_arr


print(get_multiples(1, 10, 2))


