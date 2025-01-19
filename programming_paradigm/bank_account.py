class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance=account_balance

        
    def deposit(self ,amount):
        return self.__account_balance+amount
        pass
    def withdraw(self, amount): 
        if self.__account_balance !=0:
          print("Withdrew: $",self.__account_balance-amount)
          return True
        elif self.__account_balance <= 0 & amount<self.__account_balance:
          print("Insufficient funds")
          return False
        pass
    def display_balance(self):
         print("Current Balance: $",self.__account_balance)
        

bank1=BankAccount(100)
print(bank1.deposit(0))    