import sys 

def main():
    f1=open(sys.argv[1],"r")
    f2=open(sys.argv[2],"r") 

    if (f1.read()==f2.read()):
        print("Success")
    
    else:
        print("Failure")

    f1.close()
    f2.close()

if __name__ =="__main__":
    main()