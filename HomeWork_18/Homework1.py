class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Hashvi Licqavorum ", amount)
        else:
            print("Xndrum enq mutqagrel  drakan tiv")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("duq kanxikacrel eq  ", amount)
        else:
            print("Xndrum enq mutqagrel drakan tiv.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.interest_rate / 100
        self.balance += interest
        print(f"Dzer mutqain bonusy kazmum e   {interest} ")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("kanxikacum", amount)
            else:
                print(f"Dzer pahanjac gumary  {amount - self.balance} dramov avel  e yev kgandzvi tuyj {self.overdraft_fee} dram , duq kanxikacreciq dzer amboghj gumary {self.balance}")
                self.balance = 0
                self.balance -= self.overdraft_fee
        else:
            print("Xndrum enq mutqagrel Drakan gumar")

        

savings_account = SavingsAccount(account_number="Samvel", balance=1000, interest_rate=5)
savings_account.deposit(500)

checking_account = CheckingAccount(account_number="Samvel", balance=1000, overdraft_fee=50)
checking_account.withdraw(1100)

print("Xnayoghakan Hashivi Mnacord ",savings_account.get_balance())
print("Yntacik Hashiv Mnacord", checking_account.get_balance())


