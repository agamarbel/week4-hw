class Account:
    def __init__(self,id):
        self.id = id
        self.balance =  0
        self.history = [0]

    def deposit(self,amount):
        self.balance += amount
        self.history.append(self.balance)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(self.balance)
            return amount
        else:
            return 0          
if __name__ == '__main__':
    account = Account(123)
    print(account.balance)  
    account.deposit(5234)
    print(account.balance) 
    account.deposit(500)
    print(account.balance)
    account.withdraw(2000)
    print(account.balance)
    account.withdraw(2000)
    print(account.balance) 
