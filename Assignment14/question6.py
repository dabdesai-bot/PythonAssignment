CheckOdd=lambda n :n%2==1

def main():
    a=0
    a=int(input("Enter the number"))
    result=CheckOdd(a)
    if(result==True):
        print("It is Odd number")
    else:
        print("It is Even number")

if __name__=="__main__":
    main()