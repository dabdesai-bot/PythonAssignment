def Divisble(a):
    if(a%5==0):
        return True
    else:
        return False
    
def main():
    b=0
    b=int(input("Enter the number"))
    result=0
    result=Divisble(b)
    print("It is Divisble:",result)

if __name__=="__main__":
    main()