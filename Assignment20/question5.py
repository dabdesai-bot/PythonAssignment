import threading

# Thread1 function
def thread1_task():
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    for i in range(1, 51):
        print(i, end=" ")
    print("\n")


# Thread2 function
def thread2_task():
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()


# Create threads
t1 = threading.Thread(target=thread1_task, name="Thread1")
t2 = threading.Thread(target=thread2_task, name="Thread2")

# Start Thread1
t1.start()
t1.join()      # Ensure Thread1 completes first

# Start Thread2
t2.start()
t2.join()