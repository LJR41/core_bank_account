class BankAccount:
    acc_balance = 0
    def_interest = 0.01

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.acc_balance = balance

    def deposit(self, amount):
        self.acc_balance += amount
        return self

    def withdraw(self, amount):
        if self.acc_balance > amount:
            self.acc_balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.acc_balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.acc_balance}")    
    
    def yield_interest(self):
        if self.acc_balance > 0:
            self.acc_balance * self.int_rate
        return self

Josh = BankAccount(0.05, 1000)
Ashley = BankAccount(0.02, 5000)

Josh.deposit(150).deposit(300).deposit(100).withdraw(1500).yield_interest().display_account_info()
Ashley.deposit(1000).deposit(1500).withdraw(2500).withdraw(500).withdraw(500).withdraw(250).yield_interest().display_account_info()