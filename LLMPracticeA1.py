# Chat GPT practice problem A1
class BankAccount():
    def __init__(self, owner, __balance, __overdraft_limit):
        self.owner = owner
        self.__balance = __balance
        self.__overdraft_limit = __overdraft_limit

    def deposit(self, amt):
        return self.__balance + amt

    def withdraw(self, amt):
        testBalance = self.__balance - amt
        if(testBalance < self.__overdraft_limit):
            print("Warning, exceeded overdraft limit")
            return
        elif(testBalance < 0):
            print(f"Warning, overdraft {testBalance}")
            return self.__balance - amt
        else:
            print(f"Remaining Balance: {testBalance}")
            return self.__balance - amt
    
    def setOverdraftLimit(self, limit):
        self.__overdraft_limit = limit
    
    def getBalance(self):
        return self.__balance
    
acct = BankAccount("Mark", 200, 0)
acct.withdraw(100)
print(f"Balance: {acct.getBalance}")
acct.deposit(20)
print(f"Balance: {acct.getBalance}")
acct.withdraw(200)
print(f"Balance: {acct.getBalance}")
acct.setOverdraftLimit(200)
acct.withdraw(200)