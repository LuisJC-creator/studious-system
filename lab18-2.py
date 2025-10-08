class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f"Your balance is: {self.__balance}")
        return

    def withdraw(self, amount):
        if (self.__balance - amount) < 0:
            print("Error: Negative Balance")
        else:
            self.__balance = self.__balance - amount
            print(f"Your balance: {self.__balance}")

    def get_balance():
        return self.__balance
    

acct = BankAccount(100)
acct.deposit(200)
acct.withdraw(150)
acct.withdraw(400)
