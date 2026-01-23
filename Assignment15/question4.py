from functools import reduce

Addition=lambda a,b:a+b

def main():
    data=[1,2,3,4,5]
    print("Data Generated:",data)
    Rdata=reduce(Addition,data)
    print("Addition is:",Rdata)

if __name__ =="__main__":
    main()

