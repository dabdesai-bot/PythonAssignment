def Number(a):
    if(a%3==0 & a%5==0):
        print("it is divisble by 3 and 5")
    else:
        print("it is not divisible by 3 and 5")

def main():
    x=0
    x=int(input("Enter the number"))
    result=0
    result=Number(x)
    print(result)

if __name__ =="__main__":
    main()          
