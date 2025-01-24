class BankAccount:
    def __init__(self, account_balance):
        account_balance = 0
        self.account_balance = account_balance

#method deposit       
    def deposit(self, amount):
        return self.account_balance+amount
    
#method withraw
    def withdraw(self, amount): 
        try:
            if amount < self.account_balance:
                self.account_balance -= amount
                return f"Withdrew: ${amount}"
        except Exception:
            return f"Insufficient funds."    
      
#method display balance        
    def display_balance(self):
         print("Current Balance: $",self.account_balance)
        

