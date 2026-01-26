def count_digits(num):
    sum= 0

    while num > 0:
        digit=num%10
        sum=sum+digit
        num = num // 10
    return sum

def main():
    n= int(input("Enter a number: "))
    print("Number of digits:", count_digits(n))


if __name__ =="__main__":
    main()