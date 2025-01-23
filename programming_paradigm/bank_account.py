class BankAccount:
    def __init__(self, account_balance):
        account_balance = 0
        self.account_balance = account_balance

#method deposit       
    def deposit(self, amount):
        return self.account_balance+amount
    
#method withraw
    def withdraw(self, amount): 
        if self.account_balance != 0:
          return True
          
        elif self.account_balance <= 0:
          return "Insufficient funds"
          return False
        elif amount < self.account_balance:
          return "Insufficient funds"
                
#method display balance        
    def display_balance(self):
         print("Current Balance: $",self.account_balance)
        

