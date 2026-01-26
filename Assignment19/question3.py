from functools import reduce   

def Greater(n):
    return n>=70 and n<=90

def  Additon(n):
    return n+10

def Product(a,b):
    return a*b

def main():
    data=[12,34,70,89,67,90,45,77,88,87]
    print("Data is:",data)
    Fdata=list(filter(Greater,data))
    print("The Filter data is:",Fdata)
    Mdata=list(map(Additon,Fdata))
    print("Map data is:",Mdata)
    Rdata=reduce(Product,Mdata)
    print("The reduce data:",Rdata)

if __name__ =="__main__":
    main()