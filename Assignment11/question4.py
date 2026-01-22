def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num = num//10
    return rev

number = int(input("Enter a number: "))
print("Reverse of the number:", reverse_number(number))
