def Circle(Radius):
    area=3.14*Radius*Radius
    return area

def main():
    r=0
    r=int(input("Enter the number"))
    result=0
    result=Circle(r)
    print("Area of Circle:",result)

if __name__=="__main__":
    main()