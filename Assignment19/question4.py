from functools import reduce

def EvenNumber(n):
    return n%2==0

def Square(n):
    return n*n

def Addition(a,b):
    return a+b

def main():
    data=[1,2,3,4,5,6,7,8]
    print("Data Generated is:",data)
    Fdata=list(filter(EvenNumber,data))
    print("The Filter data:",Fdata)
    Mdata=list(map(Square,Fdata))
    print("The map data:",Mdata)
    Rdata=reduce(Addition,Mdata)
    print("The Reduce data:",Rdata)

if __name__ =="__main__":
    main()