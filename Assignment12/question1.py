def Character(ch):
    if ch in 'aeiou':
        print("It is Vowel")
    else:
        print("It is constrant")

def main():
    chr=input("Enter the string") 
    Character(chr)     

if __name__=="__main__":
    main()  