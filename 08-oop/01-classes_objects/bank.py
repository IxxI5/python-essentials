# Define a base class for Bank Account
# A class is a blueprint for creating objects
# The class BankAccount has three attributes: account_number, account_name, and balance and 
# three methods: deposit, withdraw, and get_balance
class BankAccount:
    # The __init__ method is a special method that is called when a new object is created
    def __init__(self, account_number, account_name, balance=0):
        """
        Initialize a Bank Account object.

        :param account_number: Unique account number
        :param account_name: Account holder's name
        :param balance: Initial account balance (default: 0)
        """
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    # The deposit method adds money to the account
    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: Amount to deposit
        """
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}")

    # The withdraw method subtracts money from the account
    def withdraw(self, amount):
        """
        Withdraw money from the account.

        :param amount: Amount to withdraw
        """
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}")

    # The get_balance method returns the current account balance
    def get_balance(self):
        """
        Get the current account balance.

        :return: Current balance
        """
        return self.balance