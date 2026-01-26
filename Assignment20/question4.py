import threading

# Small letters thread
def count_small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Number of lowercase characters:", count)
    print()


# Capital letters thread
def count_capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Number of uppercase characters:", count)
    print()

def count_digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Number of digits:", count)
    print()


# Main program
s = input("Enter a string: ")

t1 = threading.Thread(target=count_small, args=(s,), name="Small")
t2 = threading.Thread(target=count_capital, args=(s,), name="Capital")
t3 = threading.Thread(target=count_digits, args=(s,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()