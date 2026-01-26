def min_in_list(n):
    lst = []
    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)

    minimum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
    return minimum

def main():
    n = int(input("Enter how many numbers: "))
    print("Minimum number:", min_in_list(n))

if __name__ =="__main__":
    main()
