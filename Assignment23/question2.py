class BankAccount:
    ROI=10.5

    def __init__(self,name,amount):
        self.name=name
        self.amount=amount

    def Display(self):
        print("The name of bank holder:",self.name)
        print("The Amount of bank holder:",self.amount)

    def Deposit(self,value):
        self.amount = self.amount + value
        print("the Deposited Amount:",self.amount)

    def Withdraw(self,value1):
   
        if (self.amount>value1):
            print("The Amount withdraw from account:", self.amount - value1)
        else:
            print("Not Sufficient Amount")

    def CalculateInterest(self):
        Interest=(self.amount*BankAccount.ROI)/100
        print("The Interest amount:",Interest)
    
obj1=BankAccount("Saee",20000)
obj1.Display()
obj1.Deposit(500)
obj1.Withdraw(500)
obj1.CalculateInterest()

print("----------------------------------")

obj2=BankAccount("Jannie",30000)
obj2.Display()
obj2.Deposit(1000)
obj2.Withdraw(300)
obj2.CalculateInterest()