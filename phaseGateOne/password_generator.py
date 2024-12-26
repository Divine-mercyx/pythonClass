import random

def get_password_generated():
    letter = ["a", "b", "c", "B", "A", "z", "r", "R", "3", "4", "12", "#", "8", "t", "l"]
    password = ""
    for index in range(16):
        if len(password) >= 16:
            break
        password += random.choice(letter)
    return password
    


