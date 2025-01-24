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
                print(f"Withdrew: ${self.account_balance}")
                return True
        except Exception:
            print("Insufficient funds")
            return False  
      
#method display balance        
    def display_balance(self):
         print("Current Balance: $",self.account_balance)
        

