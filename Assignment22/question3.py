class Arithematic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def accept(self):
        self.value1=int(input("Enter The number"))
        self.value2=int(input("Enter The number"))

    def Addition(self):
        return self.value1 + self.value2
    
    def Substraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        if self.value2 ==0:
            return "Division by zero is not allowed"
        else:
            return self.value1 / self.value2
        
obj1=Arithematic()
obj1.accept()
print("Addition:",obj1.Addition())
print("Substraction:",obj1.Substraction())
print("Multiplication:",obj1.Multiplication())
print("Division:",obj1.Division())
print("-------------------------------------")

obj2=Arithematic()
obj2.accept()
print("Addition:",obj2.Addition())
print("Substraction:",obj2.Substraction())
print("Multiplication:",obj2.Multiplication())
print("Division:",obj2.Division())
print("-------------------------------------")

