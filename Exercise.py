class BankAccount():
    
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def display(self):
        print(self.name, self.balance)
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

p1 = BankAccount("John")
p2 = BankAccount("Mary", 1000)

p1.display()
p2.display()

p1.withdraw(10)
p1.display()

p2.withdraw(50)
p2.display()

p1.deposit(60)
p1.display()

p2.deposit(100)
p2.display()