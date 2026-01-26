def Number(a):
    if(a>0):
        print("Positive Number")
    elif(a<0):
        print("Negative Number")
    else:
        print("Zero")

def main():
    b=0
    b=int(input("Enter the number")) 
    Number(b)

if __name__=="__main__":
    main()   