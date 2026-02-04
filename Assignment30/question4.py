def main():
    FileName1=input("Enter the File name")
    FileName2=input("Enter the File name")

    f1=open(FileName1,"r")
    f2=open(FileName2,"w")
    f2.write(f1.read())

    f1.close()
    f2.close()

    print("File Copied Successfully")


if __name__ =="__main__":
    main()