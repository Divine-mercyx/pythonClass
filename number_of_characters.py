import re

import bcrypt

def get_number(char, value):
    count = 0
    for ch in value:
        if ch == char:
            count += 1
    return count

def get_number_of_characters(value):
    if type(value) == str:
        contains = []
        my_dict = {}
        for char in value:
            if char not in contains:
                contains.append(char)
                my_dict[char] = get_number(char, value)
        return my_dict
    raise ValueError



def swap_strings(first, second):
    if type(first) == str and type(second) == str:
        temp_first = ""
        temp_second = ""
        for i in range(len(first)):
            temp_first += first[i]
            temp_second += second[i]
            if i == 1:
                temp_second += first[2:]
                temp_first += second[2:]
                break
        return f"{temp_second} {temp_first}"
    raise ValueError



def put_ce_in_word(value: str, chars: str):
    if type(value) == str and type(chars) == str:
        values = ""
        if len(value) % 2 > 0:
            value += chars
            return value
        else:
            divide_number = len(value) // 2
            return value[:divide_number] + chars + value[divide_number:]
    raise ValueError


def arrange_word(value: str):
    if type(value) == str:
        high_caps_string = ""
        low_caps_string = ""
        for char in value:
            if char.isupper(): high_caps_string += char
            else: low_caps_string += char
        return high_caps_string + low_caps_string
    raise ValueError


def get_number_of_occurence(word, item):
    if type(word) == str and type(item) == str: return (item, word.count(item))
    raise ValueError


def remove_special_characters(word: str):
    if type(word) == str:
        filtered_word = "".join(filter(str.isalnum, word))
        return filtered_word
    raise ValueError

def signup(email: str, password: str):
    if not email or not password:
        raise ValueError("Email and password cannot be empty")
    validate_email(email)
    if check_if_email_exists(email):
        raise ValueError("Email already exists")
    with open('user.txt', 'a') as f:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        f.write(f"{email.lower()} : {hashed_password.decode('utf-8')}\n")


def login(email: str, password: str):
    if not email or not password:
        raise ValueError("Email and password cannot be empty")
    validate_email(email)
    with open('user.txt', 'r') as file:
        for line in file:
            my_email, my_password = line.strip().split(' : ')
            if my_email.lower() == email.lower() and bcrypt.checkpw(password.encode('utf-8'), my_password.encode('utf-8')):
                return True
        return False


def validate_email(my_email: str):
    if not my_email:
        raise ValueError("Email cannot be empty")
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-z]+\.[a-zA-Z]{3}$'
    if not bool(re.match(email_regex, my_email)):
        raise ValueError("Invalid email format")


def check_if_email_exists(my_email: str):
    if not my_email:
        raise ValueError("Email cannot be empty")
    with open('user.txt', 'r') as file:
        for line in file:
            stored_email, _ = line.strip().split(' : ')
            if stored_email.lower() == my_email.lower():
                return True
    return False


print(login('divine@gmail.com', 'password'))

