class Account:
    def __init__(self, account_number, pin_hash, balance=0):
        self.account_number = account_number
        self.pin_hash = pin_hash
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return self.balance
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history
