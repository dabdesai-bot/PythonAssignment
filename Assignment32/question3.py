import os
import hashlib

def get_checksum(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def remove_duplicates(dir_name):
    files = {}
    log = open("Log.txt", "w")

    for file in os.listdir(dir_name):
        path = os.path.join(dir_name, file)
        if os.path.isfile(path):
            checksum = get_checksum(path)
            if checksum in files:
                os.remove(path)
                log.write(file+"deleted\n")
            else:
                files[checksum] = file

    log.close()
    print("Duplicate file names deleted to Log.txt")

def main():
    dirname = input("Enter directory name: ")
    remove_duplicates(dirname)

if __name__== "__main__":
    main()