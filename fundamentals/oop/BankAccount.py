class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    balance = 0
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(f"Balance: {self.balance}")
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance <= 0:
            print("Sorry your balance is currently empty")
        self.balance += (self.int_rate * self.balance)
        return self


ryan = BankAccount(0.05, 400)

charles = BankAccount(0.01, 5600)

ryan.deposit(300).deposit(300).deposit(300).withdraw(800).yield_interest().display_account_info()

charles.deposit(8302).deposit(45932).withdraw(10000).withdraw(453).yield_interest().display_account_info()

