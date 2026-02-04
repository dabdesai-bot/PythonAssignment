import os

def main():
    FileName=input("Enter the file name")
    f = open(FileName, "r")
    print(f.read())
    print("File gets successfully opened and display the content")
    f.close()

if __name__=="__main__":
    main()
