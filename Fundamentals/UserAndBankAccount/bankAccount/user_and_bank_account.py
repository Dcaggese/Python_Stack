class BankAccount:


    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.account_balance = balance

    def deposit(self,amount):
        self.account_balance += amount
        return self
    
    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            self.account_balance -= 5
            print(f"Insuffiscent funds. Fee of $5 charged to account.\nNew Balance is: {self.account_balance}")
        return self
    
    def display_account_info(self):
        print(f"Account Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.int_rate
        else:
            print("No interest earned")
        return self

class User:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02,0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


user1 = User("Adrien","Adrien@email.com")

user1.display_user_balance().make_deposit(250).make_withdraw(300).make_withdraw(245).make_deposit(25).display_user_balance()