def Pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():
    a=0
    a=int(input("Enter the number"))
    Pattern(a) 

if __name__ =="__main__":
    main()   