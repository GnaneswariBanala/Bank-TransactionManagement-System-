class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into Account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Insufficient balance in Account {self.account_number}")

    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


def main():
    # Create BankAccount objects
    account1 = BankAccount("A001", "Sarja", 2000)
    account2 = BankAccount("A002", "Sagar", 7000)

    # Perform transactions
    account1.display_balance()
    account1.deposit(2000)
    account1.withdraw(1000)
    account1.display_balance()

    account2.display_balance()
    account2.withdraw(5000)
    account2.display_balance()


if __name__ == "__main__":
    main()
