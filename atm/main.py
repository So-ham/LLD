from handlers import AccountHandler
from services import AccountService
from repositories import AccountRepository

class CLIDriver:
    def __init__(self, account_handler):
        self.account_handler = account_handler

    def run(self):
        while True:
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                pin = input("Enter your PIN: ")
                account = self.account_handler.create_account(pin)
                print(f"Account created successfully. Your account number is: {account.account_number}")
            elif choice == "2":
                account_number = input("Enter your account number: ")
                pin = input("Enter your PIN: ")
                account = self.account_handler.login(account_number, pin)
                if account:
                    print("Login successful")
                    self.show_account_menu(account)
                else:
                    print("Invalid account number or PIN")
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    def show_account_menu(self, account):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                amount = float(input("Enter deposit amount: $"))
                print("New Balance:", account.deposit(amount))
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: $"))
                print("New Balance:", account.withdraw(amount))
            elif choice == "3":
                print("Current Balance:", account.get_balance())
            elif choice == "4":
                print("Transaction History:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    account_repository = AccountRepository()
    account_service = AccountService(account_repository)
    account_handler = AccountHandler(account_service)
    cli = CLIDriver(account_handler)
    cli.run()
