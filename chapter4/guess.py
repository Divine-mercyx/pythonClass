import random


random_number = random.randint(1, 1000)

answer = ""

while answer.lower() != "yes":
	guess = int(input("guess my random number: "))
	if guess < random_number:
		print("Too low")
	elif guess > random_number:
		print("Too high")
	elif guess == random_number:
		print("Congratulations you got it right")
		answer = input("do you want to quit? yes or no:  ")