addition=lambda a,b : a+b

def main():
    x=0
    y=0
    x=int(input("Enter the number"))
    y=int(input("Enter the number"))
    result=addition(x,y)
    print("Addition :",result)

if __name__=="__main__":
    main()