def add_list(n):
    lst = []
    total = 0
    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)
        total=total+num
    return total

def main():
    n = int(input("Enter how many numbers: "))
    print("Addition:", add_list(n))

if __name__ == "__main__":
    main()
