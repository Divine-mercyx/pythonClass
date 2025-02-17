import sys

from myBankApp.bank import Bank

def main(logged_in_user, bank: Bank):
    prompt = """
    1 -> login
    2 -> sign up
    """
    choice = input(prompt)
    if choice == '1': login(logged_in_user, bank)
    elif choice == '2': signup(logged_in_user, bank)

def display_menu(logged_in_user, bank):
    prompt = """
    1 -> Transfer
    2 -> logout
    """
    choice = input(prompt)
    if choice == '1': transfer(logged_in_user, bank)
    elif choice == '2': sys.exit(1)

def transfer(logged_in_user, bank: Bank):
    amount = input("how much money do you want to transfer? ")
    recipient_account_number = input("enter account number: ")
    pin = input("enter pin: ")
    try:
        bank.transfer(logged_in_user, recipient_account_number, amount, pin)
        print("transfer successful")
        display_menu(logged_in_user, bank)
    except Exception as e:
        print(e)

def signup(logged_in_user, bank: Bank):
    print("=======signup=======")
    first_name = input("enter your first name: ")
    last_name = input("enter your last name: ")
    pin = input("enter your pin: ")
    create_account(first_name, last_name, pin, logged_in_user, bank)



def create_account(first_name, last_name, pin, logged_in_user, bank):
    bank.create_account(first_name, last_name, pin)
    print("Your account has been created!")
    print("login into your account")
    login(logged_in_user, bank)


def login(logged_in_user, bank: Bank):
    print("========login========")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    authenticate_user(name, password, logged_in_user, bank)


def authenticate_user(name, password, logged_in_user, bank: Bank):
    try:
        logged_in_user = bank.authenticate_user(name, password)
        print(logged_in_user)
        display_menu(logged_in_user, bank)
    except Exception as e:
        print(e)
        main(logged_in_user, bank)




logged_in_users = None
banks = Bank()

main(logged_in_users, banks)