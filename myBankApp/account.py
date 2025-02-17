def validate_account_name(account_name):
    if account_name == "" or account_name == " ": raise ValueError("Account name cannot be empty")

def validate_account_pin(account_pin):
    if account_pin == "": raise ValueError("Account pin cannot be empty")


class Account:

    def __init__(self, fullname, account_number, pin):
        self.__validate_inputs(fullname, account_number, pin)
        self.__account_name = fullname
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = 0


    def __validate_inputs(self, fullname, account_number, pin):
        validate_account_name(fullname)
        validate_account_pin(pin)

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, fullname):
        self.__account_name = fullname

    def update_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
        else: raise ValueError("Pin does not match")

    def get_account_number(self):
        return self.__account_number


    def get_account_password(self):
        return self.__pin


    def get_balance(self, pin):
        if self.__pin == pin:
            return self.__balance
        else: raise ValueError("Pin does not match")


    def deposit(self, amount):
        if amount < 0: raise ValueError("Amount cannot be negative")
        else: self.__balance += amount


    def withdraw(self, amount, pin):
        if amount < 0: raise ValueError("Amount cannot be negative")
        else: self.__balance -= amount


    def __str__(self):
        return f"Account name: {self.__account_name}\nAccount number: {self.__account_number}\nBalance: {self.__balance}"





