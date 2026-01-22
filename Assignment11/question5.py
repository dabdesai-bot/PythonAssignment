def reverse_number(num):
    a=num
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10

    if a==rev:
        print("it is palindrome number")
    else:
        print("it is not palindrome number")    

number = int(input("Enter a number: "))
reverse_number(number)
