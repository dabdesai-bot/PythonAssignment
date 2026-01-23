from functools import reduce

Product=lambda a,b: a*b

def main():
    data=[1,3,4,2]
    print("Data:",data)
    Rdata=reduce(Product,data)
    print("The Product:",Rdata)

if __name__=="__main__":
    main()