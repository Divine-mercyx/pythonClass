from myBankApp.account import Account

class Bank:

    def __init__(self):
        self.__account_number = 0
        self.__accounts = []

    def create_account(self, first_name, last_name, password):
        full_name = first_name + ' ' + last_name
        self.__account_number += 1
        account = Account(full_name, self.__account_number, password)
        self.__accounts.append(account)
        return account

    def transfer(self, sender: Account, receiver_account_number, amount, pin):
        validate_account_number_and_amount(receiver_account_number, amount, pin)
        receiver = self.find_account_by_account_number(receiver_account_number)
        if amount > sender.get_balance(pin): raise ValueError("insufficient funds")
        sender.withdraw(amount, pin)
        receiver.deposit(amount)

    def find_account_by_account_number(self, account_number):
        if account_number is None or not str(account_number).strip(): raise ValueError("Account Number cannot be empty.")
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        raise ValueError("Account not found.")


    def authenticate_user(self, name, password):
        if len(self.__accounts) == 0: raise ValueError("no account found")
        for account in self.__accounts:
            if account.account_name == name and account.get_account_password() == password: return account
        raise ValueError("incorrect name or password")








def validate_account_number_and_amount(receiver_account_number, amount, pin):
    validate_account_number(receiver_account_number)
    validate_pin(pin)
    validate_amount(amount)

def validate_account_number(sender_account_number):
    if sender_account_number is None or not str(sender_account_number).strip(): raise ValueError("Account Number cannot be empty.")

def validate_amount(amount):
    if amount is None or amount < 1: raise ValueError("Amount cannot be less than or equal to 1.")

def validate_pin(pin):
    if pin is None or not str(pin).strip(): raise ValueError("Pin cannot be empty.")




