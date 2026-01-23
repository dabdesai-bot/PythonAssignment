largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    print("Largest number:", largest(x, y, z))

if __name__=="__main__":
    main()