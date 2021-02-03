class BankAccount:
	def __init__(self, name, int_rate, balance,account): 
		self.name = name
		self.int_rate = int_rate
		self.balance= balance
		self.account= account

	def deposit(self, deposit):
		self.balance += deposit
		return self
	
	def withdraw(self, withdraw):
		self.balance -= withdraw
		return self

	def yieldinterest(self):
		if self.balance>0:
			self.balance += self.balance * self.int_rate
		return self

	def display_account_info(self):
		print(f"name: {self.name}, balance: {self.balance}")
		return self

		

A1= BankAccount( "Mike", 0.10, 500, "Checking")
A2= BankAccount("Whitney",0.01, 3400, "Checking")
print(A1.balance)

A1.deposit(100).deposit(50).deposit(40).withdraw(20).display_account_info().yieldinterest().display_account_info()
A2.deposit(200), A2.deposit(400), A2.withdraw(200), A2.withdraw(200), A2.withdraw(400), A2.withdraw(200), A2.display_account_info()