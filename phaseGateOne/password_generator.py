import random

def get_password_generated():
    letter = ["@", "x", "L", "%", "b", "Q", "y", "Z", "u", "A"]
    numbers = ["6", "5", "8","9"]
    password = ""
    for index in range(16):
        number = str(random.randrange(100))
        if len(password) >= 16:
            break
        password = str(number) + password
        password = letter[index] + password
        number =int(number)
        password = str(number // 3) + password
    return password
    


