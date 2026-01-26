def ChkPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# function to return sum of prime numbers from list
def ListPrime(lst):
    total = 0
    for num in lst:
        if ChkPrime(num):
            total += num
    return total


# main program
def main():
    n = int(input("Enter number of elements: "))
    lst = []

    print("Enter elements:")
    for i in range(n):
        lst.append(int(input()))

    result = ListPrime(lst)
    print("Sum of prime numbers:", result)

if __name__ =="__main__":
    main()