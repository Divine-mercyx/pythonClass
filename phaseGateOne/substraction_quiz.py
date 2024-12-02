import random
import datetime
import time

"""
get the current datetime and store it as start_time
create a counter variable and assign zero to it
create a score variable and assign zero to it
while counter is less than 10
generate a random number between 100
store it as first_number
generate a random number between 100
store it as second number
create a variable and store it as correct_answer
assign zero to it
if second_number > first_number
display 1 question: second_number - first_number
correct_answer = second_number - first_number
else display first_number - second_number
correct_answer = first_number - second_number
prompt the user to enter an answer
collect the answer and store the answer as answer
if answer == correct_answer
score increments by one
increment counter

get the current datetime and store it as end_time
display you start time is start_time / your end time is end_time/ you scored score / 10
"""

counter = 1
score = 0

start_time = datetime.datetime.now()
print(start_time)
while counter <= 10:
    first_number = random.randrange(100)
    second_number = random.randrange(100)
    correct_answer = 0
    if second_number > first_number:
        print(f"{counter}. question: {second_number} - {first_number}")
        correct_answer = second_number - first_number
    else:
        print(f"{counter}. {first_number} - {second_number}")
        correct_answer = first_number - second_number
    answer = int(input("answer: "))
    if answer == correct_answer:
        score += 1
    counter += 1
end_time = datetime.datetime.now()
print(f"your start time: {start_time}\nYour end time: {end_time}\nyou scored {score} / 10")
