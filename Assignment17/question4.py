def find_factors(n):
    sum=0
    print("Factors of", n, "are:")
    for i in range(1, n+ 1):
        if n % i == 0:
            sum=sum+i
    return sum

def main():
    a=0 
    a=int(input("Enter the number"))
    result=0
    result=find_factors(a)
    print("The Sum of factor:",result)
    
if __name__ =="__main__":
    main()
