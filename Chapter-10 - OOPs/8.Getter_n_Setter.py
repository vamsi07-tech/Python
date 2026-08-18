class BankAccount:
    def __init__ (self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance (self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")

account = BankAccount(10000)
print(account.balance)
account.balance = 50000
print(account.balance)