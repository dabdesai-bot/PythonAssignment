def ChkGreater(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")

def main():
    x=0
    y=0
    x=int(input("Enter the number"))
    y=int(input("Enter the number"))
    result=0
    result=ChkGreater(x,y)
    print(result)

if __name__=="__main__" :
    main()           