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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.05, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(self.account.balance)
        return self
    def transfer_money(self, amount, other_user):
        self.other_user = other_user
        self.account.balance -= amount
        other_user.account.balance += amount
        print("Transaction complete")
        print(self.account.balance)
        print(self.other_user.account.balance)
        return self

# ryan = BankAccount(0.05, 400)

# charles = BankAccount(0.01, 74328)

# ryan.deposit(300).deposit(300).deposit(300).withdraw(800).yield_interest().display_account_info()

# charles.deposit(8302).deposit(45932).withdraw(10000).withdraw(453).yield_interest().display_account_info()

joon = User("Ryan", "ryanjnam@yahoo.com")
joon.make_deposit(200).make_deposit(3029).make_withdrawal(922).display_user_balance()
charles = User ("Charles", "cnammd@yahoo.com")
charles.make_deposit(3000).display_user_balance()
joon.transfer_money(200, charles)
