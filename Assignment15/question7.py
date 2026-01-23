Greater=lambda a : len(a)>5

def main():
    data=["mango","tree","Apple","PineApple"]
    print("Data is:",data)
    Fdata=list(filter(Greater,data))
    print("The Filter data :",Fdata)

if __name__=="__main__":
    main()    