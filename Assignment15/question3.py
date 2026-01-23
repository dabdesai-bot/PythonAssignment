CheckOdd=lambda a: (a%2==1)

def main():
    data=[10,23,30,43,50]
    print("Data:",data)
    Fdata=list(filter(CheckOdd,data))
    print("After Filter data:",Fdata)

if __name__=="__main__":
    main()