def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def main():
    num = int(input("Enter a number: "))
    print("Factorial is:", factorial(num))

if __name__ =="__main__":
    main()
