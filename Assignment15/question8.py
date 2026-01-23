Divisble=lambda a: a%3==0 and a%5==0

def main():
    data=[10,15,20,25,30]
    print("Data:",data)
    Fdata=list(filter(Divisble,data))
    print("The Filter data :",Fdata)

if __name__=="__main__":
    main()