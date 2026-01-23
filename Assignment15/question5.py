from functools import reduce

Maximum= lambda a,b: a if a>b else b

def main():
    data=[10,20,3,6,50]
    print("Data generated:",data)
    Rdata=reduce(Maximum,data)
    print("Maximum number:",Rdata)

if __name__=="__main__":
    main()    