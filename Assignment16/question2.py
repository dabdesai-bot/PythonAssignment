def  ChkNum(a):
    if(a%2==0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    b=0
    b=int(input("Enter the number"))
    ChkNum(b)

if __name__=="__main__":
    main()