class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient balance. Available: {self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")

    def show(self):
        print(f"Account holder: {self.holder} | Balance: {self.balance:.2f}")


holder = input("Enter account holder name: ")
balance = float(input("Enter opening balance: "))
account = BankAccount(holder, balance)
account.show()

account.deposit(float(input("Enter amount to deposit: ")))
account.withdraw(float(input("Enter amount to withdraw: ")))
account.show()
