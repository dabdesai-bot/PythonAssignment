def Number(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

a=0
a=int(input("Enter the number"))
result=0
result=Number(a)
print(result)