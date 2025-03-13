# main.py is the main entry point of the application
# main.py imports the BankAccount, CheckingAccount, and SavingsAccount classes 
# from the bank, checking_account, and savings_account modules
# and creates account objects and performs transactions

# Import the account classes
from bank import BankAccount
from checking_account import CheckingAccount
from savings_account import SavingsAccount

# Create account objects
account1 = BankAccount("12345", "John Doe", 1000)
account2 = CheckingAccount("67890", "Jane Doe", 500, 2000)
account3 = SavingsAccount("34567", "Bob Smith", 2000, 0.05)

# Perform transactions
account1.deposit(500)
account2.withdraw(200)
account3.add_interest()

# Print account balances
print(f"Account 1 balance: ${account1.get_balance():.2f}")
print(f"Account 2 balance: ${account2.get_balance():.2f}")
print(f"Account 3 balance: ${account3.get_balance():.2f}")

# Output:
# Account 1 balance: $1500.00
# Account 2 balance: $300.00
# Account 3 balance: $2100.00