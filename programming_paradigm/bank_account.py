class BankAccount:
    """
    A simple bank account class that supports deposits, withdrawals, and balance display.
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional initial balance.
        
        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit. Should be positive.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to withdraw.
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
        """
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
