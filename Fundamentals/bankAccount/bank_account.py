class BankAccount:


    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.account_balance = balance

    def deposit(self,amount):
        self.account_balance += amount
        return self
    
    def withdraw(self,amount):
        self.account_balance -= amount
        return self
    
    def display_account_info(self):
        print(self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.int_rate
        else:
            print("No interest earned")
        return self

account1 = BankAccount(0.015,50)
account2 = BankAccount(0.015,0)

account1.display_account_info().deposit(50).deposit(200).deposit(50).withdraw(325).yield_interest().display_account_info()
# Balance should display $25.375

account2.display_account_info().deposit(1000).deposit(500).withdraw(250).withdraw(250).withdraw(250).yield_interest().display_account_info()
#balance should display $761.25


