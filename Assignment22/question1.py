class Demo:
    value=10

    def __init__(self,a,b):
        print("Inside Constructor")
        self.no1=a
        self.no2=b

    def fun(self):
        print("Inside The Fun:",self.no1,self.no2)

    def gun(self):
        print("Inside The Gun:",self.no1,self.no2)

print("Class Variable is:",Demo.value)

obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()
