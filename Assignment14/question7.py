divisble= lambda a : a%5==0

def main():
    b=0
    b=int(input("Enter the number"))
    result=divisble(b)
    if(result==True):
        print("it is divisble by 5")
    else:
        print("it is not divisble by 5")

if __name__=="__main__":
    main()

