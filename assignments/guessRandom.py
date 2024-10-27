import random

lucky_guess = random.randint(1, 50)

guess = 0

while guess != lucky_guess:
    guess = int(input("guess a number: "))
    if guess > lucky_guess:
        print("too high, try again")
    elif guess < lucky_guess:
        print("too low, try again")
    elif guess == lucky_guess:
        print("you won")