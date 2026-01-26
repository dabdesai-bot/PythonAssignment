from functools import reduce

def PrimeNumber(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if (n%i==0):
            return False
    return True
    
def product(n):
    return n*2

def Maximum(a,b):
    return a if a>b else b

def main():
    data=[2,3,4,5,6,7,8]
    print("Data generated:",data)
    Fdata=list(filter(PrimeNumber,data))
    print("The filter data is:",Fdata)
    Mdata=list(map(product,Fdata))
    print("the map data is:",Mdata)
    Rdata=reduce(Maximum,Mdata)
    print("The reduce value is:",Rdata)

if __name__ =="__main__":
    main()