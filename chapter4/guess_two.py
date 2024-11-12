import random


random_number = random.randint(1, 1000)

answer = ""

count = 0
while answer.lower() != "yes":
	
	guess = int(input("guess my random number: "))
	if guess < random_number:
		print("Too low")

	elif guess > random_number:
		print("Too high")

	count += 1

	elif guess == random_number:
		print("Congratulations you got it right")
		answer = input("do you want to quit? yes or no:  ")

	if count == 10 or count < 10:
		print("either you know the secret or you got lucky!")

	elif count > 10:
		print("you should be able to do better")