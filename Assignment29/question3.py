import sys

def main():
    f1=open(sys.argv[1],"r")
    f2=open(sys.argv[2],"w")
    f2.write(f1.read())

    f1.close()
    f2.close()

    print("File Copied Successfully")


if __name__ =="__main__":
    main()