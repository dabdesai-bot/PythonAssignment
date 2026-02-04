import sys

def main():
    f = open(sys.argv[1], "r")
    data = f.read()

    word = sys.argv[2]

    count = data.count(word)

    print("Count:", count)

    f.close()

if __name__ =="__main__":
    main()