def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

a=0 
a=int(input("Enter the number"))
result=0
result=factorial(a)
print(result)