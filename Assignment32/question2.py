import os
import hashlib

def get_checksum(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def find_duplicates(dir_name):
    files = {}
    log = open("Log.txt", "w")

    for file in os.listdir(dir_name):
        path = os.path.join(dir_name, file)
        if os.path.isfile(path):
            checksum = get_checksum(path)
            if checksum in files:
                log.write(file + "\n")
            else:
                files[checksum] = file

    log.close()
    print("Duplicate file names written to Log.txt")

def main():
    dirname = input("Enter directory name: ")
    find_duplicates(dirname)

if __name__ == "__main__":
    main()