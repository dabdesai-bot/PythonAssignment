square= lambda a:a*a

def main():
    data=[1,2,3,4,5,6]
    print("Data is:",data)
    Mdata=list(map(square,data))
    print("Data after mapping is:",Mdata)

if __name__=="__main__":
    main()