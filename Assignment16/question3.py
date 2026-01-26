def Add(a,b):
    ans=a+b
    return ans

def main():
    x=0
    y=0
    x=int(input("Enter the number"))
    y=int(input("Enter the number"))
    result=0
    result=Add(x,y)
    print("Addition :",result)

if __name__=="__main__":
    main()
    