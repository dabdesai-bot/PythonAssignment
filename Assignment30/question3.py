def main():
    FileName=input("Enter the File Name:")
    fname=open(FileName,"r")
    print(fname.read())
    print("File content are displayed Correctly")
    fname.close()



if __name__ =="__main__":
    main()