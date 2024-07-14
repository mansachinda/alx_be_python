# 0. Create a Simple Bank Account Class
# Program with BankAccount class with deposit() and withdraw() function

# Create BankAccount class
class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

# Create Deposit() function
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

# Create Withdraw() function
    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance :.2f}")

