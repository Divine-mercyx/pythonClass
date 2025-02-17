import unittest
from myBankApp.account import Account

class TestAccount(unittest.TestCase):


    def test_to_account_object_to_get_fullname(self):
        account = Account("firstname lastname", "1", "abc")
        actual = account.account_name
        expected = "firstname lastname"
        self.assertEqual(actual, expected)

    def test_that_account_object_balance_is_zero(self):
        account = Account("firstname lastname", "1", "abc")
        actual = account.get_balance("abc")
        expected = 0
        self.assertEqual(actual, expected)

    def test_to_get_balance_with_invalid_pin(self):
        account = Account("firstname lastname", "1", "abc")
        self.assertRaises(ValueError, account.get_balance, "abcd")

    def test_to_deposit_then_check_account_object_balance_deposit(self):
        account = Account("firstname lastname", "1", "abc")
        account.deposit(100)
        actual = account.get_balance("abc")
        expected = 100
        self.assertEqual(actual, expected)

    def test_to_deposit_then_withdraw_then_check_account_object_balance_withdraw(self):
        account = Account("firstname lastname", "1", "abc")
        account.deposit(100)
        account.withdraw(75, "abc")
        actual = account.get_balance("abc")
        expected = 25
        self.assertEqual(actual, expected)

    def test_to_update_pin_then_withdraw_and_check_account_object_balance(self):
        account = Account("firstname lastname", "1", "abc")
        account.deposit(100)
        account.update_pin("abc", "123")
        actual = account.get_balance("123")
        expected = 100
        self.assertEqual(actual, expected)

    def test_to_update_pin_with_invalid_oldpin(self):
        account = Account("firstname lastname", "1", "abc")
        account.deposit(100)
        actual = account.get_balance("abc")
        expected = 100
        self.assertEqual(actual, expected)
        self.assertRaises(ValueError, account.update_pin, "abcd", "123")

    def test_to_update_object_fullname(self):
        account = Account("firstname",  "1", "abc")
        actual = account.account_name
        expected = "firstname"
        self.assertEqual(actual, expected)
        account.account_name = "newname"
        actual = account.account_name
        expected = "newname"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
