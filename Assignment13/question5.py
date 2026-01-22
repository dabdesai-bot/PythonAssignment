def Marks_Student(marks):
    if(marks>=75):
        print("Distinction")
    elif(marks>=60):
        print("First Class")
    elif(marks>=50):
        print("Second Class")
    else:
        print("Fail")

def main():
    m=0
    m=int(input("Enter the number"))
    Marks_Student(m)

if __name__=="__main__":
    main()