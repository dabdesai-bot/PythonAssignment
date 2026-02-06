import sys
import os

def DirectoryFile(directory,extension):
    print("Files Found:")
    for file in os.listdir(directory):
        if file.endswith(extension):
            print(file)

def main():
    directory=sys.argv[1]
    extension=sys.argv[2]
    DirectoryFile(directory,extension)


if __name__=="__main__":
    main()