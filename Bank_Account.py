class BankAccount():
    def __init__(self,accountholder,balance):
        self.accountholder=accountholder
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance + amount
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance=self.balance - amount
            print("Withdraw Succeful")
        else:
            print("Insufficient balance")

account=BankAccount("sakthi",5000)

account.deposit(4000)
account.withdraw(2000)

print("Account Holder:",account.accountholder)
print("Final Balance:",account.balance)


        