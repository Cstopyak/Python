class User:
    def __init__(self, nameInput, emailInput):
        self.name = nameInput
        self.email = emailInput
        self.checkings = BankAccount(0.05, 0)
        self.savings = BankAccount(0.10, 100)


    def deposit(self, amount, chosenAccount):
        if chosenAccount == "checkings":
            self.checkings.deposit(amount)
        elif chosenAccount == "savings":
            self.savings.deposit(amount)         
        return self

    def withdraw(self, amount, chosenAccount):
        if chosenAccount == "checkings":
            self.checkings.deposit(amount)
        elif chosenAccount == "savings":
            self.savings.deposit(amount)         
        return self

    # def transfer(self, amount, receiver):
    #     self.withdraw(amount)
    #     receiver.deposit(amount)
    #     return self

    # def displayBalance(self):
    #     print(f"{self.name} has a balance is ${self.account}")
    #     return self


class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        return self


    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance-=amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance+= self.balance * self.interest_rate 
        return self



user1 = User("Lebron", "lbj@nba.com")
user2 = User("Kobe", "kobe@nba.com")
user3 = User("Steph", "steph@nba.com")

user1.deposit(10, "checkings")
user1.deposit(110, "savings")
user1.checkings.display_account_info()
user1.savings.display_account_info()
# user1.deposit(10).deposit(10).deposit(10).withdraw(100).displayBalance()
 
 