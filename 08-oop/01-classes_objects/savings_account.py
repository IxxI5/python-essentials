# Import the BankAccount class from bank.py
from bank import BankAccount

# Define a subclass from BankAccount for Savings Account
# The reason for creating this class is to extend the functionality of the BankAccount class
class SavingsAccount(BankAccount):
    # __init__ method to initialize the SavingsAccount object
    def __init__(self, account_number, account_name, balance=0, interest_rate=0.02):
        """
        Initialize a Savings Account object.

        :param account_number: Unique account number
        :param account_name: Account holder's name
        :param balance: Initial account balance (default: 0)
        :param interest_rate: Interest rate (default: 0.02)
        """
        super().__init__(account_number, account_name, balance)
        self.interest_rate = interest_rate

    # add_interest method to add interest to the account balance
    def add_interest(self):
        """
        Add interest to the account balance.
        """
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added ${interest:.2f} interest to account {self.account_number}")