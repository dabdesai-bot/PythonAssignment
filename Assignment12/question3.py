def Addition(a,b):
    return a+b

def Substraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    return a/b

def main():
    x=0
    x=int(input("Enter the first number"))
    y=0
    y=int(input("Enter the second number"))
    
    result=Addition(x,y)
    result1=Substraction(x,y)
    result2=Multiplication(x,y)
    result3=Division(x,y)
    print("Addition :",result) 
    print("Substraction:",result1) 
    print("Multiplication:",result2) 
    print("Division :",result3) 

if __name__=="__main__":
    main()