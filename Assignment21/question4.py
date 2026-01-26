import threading

sum_result = 0
product_result = 1

# Thread to calculate sum
def calculate_sum(lst):
    global sum_result
    sum_result = sum(lst)

# Thread to calculate product
def calculate_product(lst):
    global product_result
    product_result = 1
    for i in lst:
        product_result *= i


# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

t1 = threading.Thread(target=calculate_sum, args=(lst,))
t2 = threading.Thread(target=calculate_product, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum of elements:", sum_result)
print("Product of elements:", product_result)