import random

def get_questions(answer):
	guess_answer = random_one * random_two
	if answer == guess_answer:
		return "very good!"
	else:
		return "No. please try again"

while answer == guess_answer:
	random_one = random.randint(12)
	random_two = random.randint(12)
