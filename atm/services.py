from hashlib import sha256
from entities import Account

class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, pin):
        pin_hash = sha256(pin.encode()).hexdigest()
        account_number = self.account_repository.generate_account_number()
        return self.account_repository.create_account(account_number, pin_hash)

    def login(self, account_number, pin):
        account = self.account_repository.get_account(account_number)
        if account and account.pin_hash == sha256(pin.encode()).hexdigest():
            return account
        return None
