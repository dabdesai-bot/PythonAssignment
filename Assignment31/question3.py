import sys
import os
import shutil

def CopyDirectory(directoryName,directoryName1,extension):
    if not os.path.exists(directoryName1):
        os.mkdir(directoryName1)

    for file in os.listdir(directoryName):
        if file.endswith(extension):
            directoryName = os.path.join(directoryName, file)
            directoryName1 = os.path.join(directoryName1, file)
            shutil.copy(directoryName, directoryName1)

    print("File copied Successfully")         

def main():
    directoryName=sys.argv[1]
    directoryName1=sys.argv[2]
    extension=sys.argv[3]

    CopyDirectory(directoryName,directoryName1,extension)

if __name__=="__main__":
    main()      