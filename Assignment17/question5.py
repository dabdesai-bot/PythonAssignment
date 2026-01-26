def PrimeNumber(n):
    for i in range(2,n+1):
        if (n%2==0):
            return False
    return True   

def main():
    a=0
    a=int(input("Enter the number"))
    if PrimeNumber(a):
        print(a,"is a prime number")
    else:
        print(a,"is not a prime number")  

if __name__ == "__main__":
    main()