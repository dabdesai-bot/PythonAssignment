def main():
    FileName=input("Enter the File Name:")

    f=open(FileName,"r")
    count=0

    for line in f:
        count=count+1
        print("Total Amount of line:",count)

    f.close()

if __name__ =="__main__":
    main()