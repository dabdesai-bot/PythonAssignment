def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

def Mult(a,b):
    return a*b

def Div(a,b):
    return a/b

def main():
    x=0
    y=0
    x=int(input("Enter the  number"))
    y=int(input("Enter the  number"))
    result1=Add(x,y)
    result2=Sub(x,y)
    result3=Mult(x,y)
    result4=Div(x,y)
    print("Addition:",result1)
    print("Substraction",result2)
    print("Multiplication:",result3)
    print("Division:",result4)

if __name__ == "__main__":
    main()