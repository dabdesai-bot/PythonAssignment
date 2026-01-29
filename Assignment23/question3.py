class Numbers:
    # constructor
    def __init__(self, value):
        self.value = value   # instance variable

    # check prime
    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value / 2) + 1):
            if self.value % i == 0:
                return False
        return True

    # display all factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

    # return sum of factors
    def SumFactors(self):
        total = 0
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                total += i
        return total
    
    def ChkPerfect(self):
        sum_fact = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                sum_fact += i
        if sum_fact == self.value:
            return True
        else:
            return False


# Create multiple objects
obj1 = Numbers(6)
obj2 = Numbers(7)

# Call methods
print("Is Prime:", obj1.ChkPrime())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())
print("Is Perfect:", obj1.ChkPerfect())

print()

print("Is Prime:", obj2.ChkPrime())
obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())
print("Is Perfect:", obj2.ChkPerfect())