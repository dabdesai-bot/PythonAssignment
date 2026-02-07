class Demo:
    no=10                       #class Variable                 
    def __init__(self,a,b):           
        self.value1=a                 
        self.value2=b           #instance variable
    
    def fun(self):              #instance method
        print("Inside instance method fun:",self.value1,self.value2)

   
    @classmethod                 #decorator
    def sun(cls):               #class method
        print("inside class method sun:",cls.no)
 
    @staticmethod             #decorator Optional to use
    def gun():                 #static method
        print("Inside Static method gun:",Demo.no)

Demo.sun()

 
print("class Variable no:",Demo.no)

obj=Demo(11,21)

obj.fun()
print("Instance variable:",obj.value1,obj.value2)

Demo.gun()



