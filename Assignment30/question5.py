def main():
    Word=input("Enter the file name:")
    f=open("demo.txt","r")
    data=f.read()

    if Word in data:
        print("Found")

    else:
        print("Not Found")

if __name__ =="__main__":
    main()