maximum=lambda a,b : a if a>b else b

def main():
    x=0
    y=0
    x=int(input("Enter the number"))
    y=int(input("Enter the number"))
    print("Maximum number:",maximum(x,y))

if __name__=="__main__":
    main()
