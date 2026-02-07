import os
import time

def remove_duplicates(folder):
    files = []
    log = open("Log.txt", "w")

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            if file in files:
                os.remove(path)
                log.write(file + " deleted\n")
            else:
                files.append(file)

    log.close()

def main():
    start = time.time()

    dirname = input("Enter directory name: ")
    remove_duplicates(dirname)

    end = time.time()
    print("Execution time:", end - start)

if __name__== "__main__":
    main()