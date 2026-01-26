def max_in_list(n):
    lst = []
    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)

    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum

def main():
    n = int(input("Enter how many numbers: "))
    print("Maximum number:", max_in_list(n))

if __name__ =="__main__":
    main()
