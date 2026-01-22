def Rectangle(lenght,width):
    area=lenght*width
    return area

def main():
    l=0
    l=int(input("Enter the number"))
    w=0
    w=int(input("Enter the number"))
    result=0
    result=Rectangle(l,w)
    print("Area of rectangle:",result)

if __name__=="__main__":
    main()