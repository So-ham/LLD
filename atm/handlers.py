class AccountHandler:
    def __init__(self, account_service):
        self.account_service = account_service

    def create_account(self, pin):
        return self.account_service.create_account(pin)

    def login(self, account_number, pin):
        return self.account_service.login(account_number, pin)
