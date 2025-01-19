class BankAccount:
    def __init__(self, account_balance):
        self.account_balance=account_balance

        
    def deposit(self ,amount):
        return self.account_balance+amount
        pass
    def withdraw(self, amount):
        if amount !=0:
          print("Withdrew: $",self.account_balance-amount)
          return True
        elif amount==0:
          print("Insufficient funds")
          return False
        pass
    def display_balance(self):
         print("Current Balance: $",self.account_balance)
        

#bank1=BankAccount(100)
#print(bank1.deposit(10))    