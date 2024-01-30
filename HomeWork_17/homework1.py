# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.




class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Hashvi Licqavorum",amount)
        else:
            print("Xndrum enq mutqagrel  drakan tiv")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Kanxikacum",  amount)
            else:
                print(f"Dzer pahanjac gumary  {amount - self.balance} dramov avel  e :  Duq kanxikacreciq dzer amboghj gumary {self.balance}")
        else:
            print("Xndrum enq mutqagrel drakan tiv.")

    def get_balance(self):
        return self.balance

account1 = BankAccount(account_holder="Samvel", balance=1000)
account1.deposit(500)
account1.withdraw(9200)
print("Account Holder",account1.account_holder)
print("Mnacord ", account1.get_balance())