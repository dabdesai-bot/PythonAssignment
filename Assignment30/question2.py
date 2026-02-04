def main():
    FileName=input("Enter the File Name:")

    f=open(FileName,"r")
    count=0

    for line in f:
        words=line.split()
        count=count+len(words)
        print("Total Amount of Words:",count)

    f.close()

if __name__ =="__main__":
    main()