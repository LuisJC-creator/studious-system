class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance():
        return self.__balance
    

acct = BankAccount(100)
acct.deposit(200)
acct.withdraw(150)
acct.withdraw(400)
