def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum=sum+i

    if sum == n:
        print("Perfect number")
    else:
        print("Not a perfect number")

num = int(input("Enter a number: "))
perfect_number(num)
