import threading

# Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True


# Prime thread function
def prime_list(lst):
    print("Prime Numbers:")
    for i in lst:
        if is_prime(i):
            print(i, end=" ")
    print()


# Non-Prime thread function
def nonprime_list(lst):
    print("Non-Prime Numbers:")
    for i in lst:
        if not is_prime(i):
            print(i, end=" ")
    print()


# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

t1 = threading.Thread(target=prime_list, args=(lst,))
t2 = threading.Thread(target=nonprime_list, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()