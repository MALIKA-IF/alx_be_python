class BankAccount:
    def __init__(self, account_balance):
        self.account_balance=0

        
    def deposit(self ,amount):
        return self.account_balance+amount
        pass
    def withdraw(self, amount):
        if amount !=0:
          return self.account_balance-amount
        elif amount==0:
          return False
        pass
    def display_balance(self):
        return self.account_balance
        pass