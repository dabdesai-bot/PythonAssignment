def number(n):
    for i in range(1,n+1):
        if(i%2==1):
            print(i)       

def main():
    a=0 
    a=int(input("Enter the number"))
    number(a) 

if __name__=="__main__":
    main()           