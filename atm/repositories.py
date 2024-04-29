import uuid
from entities import Account

class AccountRepository:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin_hash):
        account = Account(account_number, pin_hash)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def generate_account_number(self):
        return str(uuid.uuid4().int)[:10]  # Generate random 10-digit account number
