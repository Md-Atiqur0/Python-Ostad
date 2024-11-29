class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        return amount
    def get_balance(self):
        return self.balance
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return print(f"Insufficient Balance")

atik = Banking("Atik",10000)
print(f"Account Name : {atik.name}")
print(f"Initial Balance : {atik.balance}")
print(f"Deposit Balance : {atik.deposit(1000)}")
print(f"After Deposit, Your Balance is : {atik.get_balance()}")
print(f"Withdraw Balance : {atik.withdraw(2000)}")
print(f"After Withdraw,Your Balance is : {atik.get_balance()}")