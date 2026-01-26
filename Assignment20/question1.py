import threading

def EvenNumber():
    print("Even Number:")
    for i in range(1,21):
        if (i%2==0):
            print(i)

def OddNumber():
    print("Odd number:")
    for i in range(1,21):
        if (i%2==1):
            print(i)

def main():
    Even=threading.Thread(target=EvenNumber())
    Odd=threading.Thread(target=OddNumber())

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    print("Both thead finish Execution")

if __name__=="__main__":
    main()

    
 