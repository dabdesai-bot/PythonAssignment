def find_frequency(n, key):
    lst = []
    count = 0

    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)
        if num == key:
            count = count+ 1

    return count

def main():
    n = int(input("Enter how many numbers: "))
    key = int(input("Enter the number to find frequency: "))

    print("Frequency:", find_frequency(n, key))

if __name__ =="__main__":
    main()
