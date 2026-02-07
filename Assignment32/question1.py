import os
import hashlib
import sys

def CalculateCheckSum(FileName):           
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName):
    ret=False
    ret= os.path.exists(DirectoryName)

    if (ret==False):
        print("There is no such directory")
        return
    
    ret=os.path.isdir(DirectoryName)

    if (ret==False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName ,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            CheckSum=CalculateCheckSum(fname)

            print(f"File Name:{fname} Check sum:{CheckSum}")




def main():
    DirectoryName=sys.argv[1]
    DirectoryWatcher(DirectoryName)


if __name__ =="__main__":
    main()