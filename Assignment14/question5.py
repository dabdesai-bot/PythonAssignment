CheckEven=lambda n :n%2==0

def main():
    a=0
    a=int(input("Enter the number"))
    result=CheckEven(a)
    if(result==True):
        print("It is Even number")
    else:
        print("It is odd number")

if __name__=="__main__":
    main()