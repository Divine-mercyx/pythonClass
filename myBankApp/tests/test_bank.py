import unittest
from myBankApp.bank import *


class TestBank(unittest.TestCase):

    def test_to_create_account_in_bank(self):
        bank = Bank()
        account = bank.create_account("firstname", "lastname", "pin")
        self.assertEqual(account.account_name, "firstname lastname")

    def test_to_create_account_in_bank_with_empty_pin_and_empty_firstname_and_lastname(self):
        bank = Bank()
        with self.assertRaises(ValueError):
            bank.create_account("firstname", "lastname", "")
        with self.assertRaises(ValueError):
            bank.create_account("", "", "pin")


    def test_to_create_account_in_bank_get_account_balance(self):
        bank = Bank()
        account = bank.create_account("firstname", "lastname", "pin")
        self.assertEqual(account.get_balance("pin"), 0)

    def test_to_create_account_in_bank_get_account_balance_with_empty_pin(self):
        bank = Bank()
        account = bank.create_account("firstname", "lastname", "pin")
        with self.assertRaises(ValueError):
            account.get_balance("pins")


    def test_to_create_account_in_bank_then_find_account_with_account_number(self):
        bank = Bank()
        account1 = bank.create_account("firstname", "lastname", "pin")
        account2 = bank.find_account_by_account_number(account1.get_account_number())
        self.assertEqual(account1, account2)

    def test_to_create_account_in_bank_then_find_account_with_invalid_account_number(self):
        bank = Bank()
        account1 = bank.create_account("firstname", "lastname", "pin")
        with self.assertRaises(ValueError):
            bank.find_account_by_account_number("")



if __name__ == '__main__':
    unittest.main()
