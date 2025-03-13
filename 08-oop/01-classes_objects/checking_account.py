# Import the BankAccount class from bank.py
from bank import BankAccount

# Define a subclass from BankAccount for Checking Account
# The reason for creating this class is to extend the functionality of the BankAccount class
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0, overdraft_limit=1000):
        """
        Initialize a Checking Account object.

        :param account_number: Unique account number
        :param account_name: Account holder's name
        :param balance: Initial account balance (default: 0)
        :param overdraft_limit: Overdraft limit (default: 1000)
        """
        super().__init__(account_number, account_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Withdraw money from the account, considering overdraft limit.

        :param amount: Amount to withdraw
        """
        if amount > self.balance + self.overdraft_limit:
            print("Transaction exceeds overdraft limit")
        else:
            super().withdraw(amount)