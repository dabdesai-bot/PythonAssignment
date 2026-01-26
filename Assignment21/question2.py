import threading

# Thread to find maximum element
def find_max(lst):
    print("Maximum element:", max(lst))


# Thread to find minimum element
def find_min(lst):
    print("Minimum element:", min(lst))


# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

t1 = threading.Thread(target=find_max, args=(lst,))
t2 = threading.Thread(target=find_min, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()