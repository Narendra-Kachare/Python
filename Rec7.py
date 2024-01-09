"""
Recurssion

"""
import sys

def Display(i):
    if (i < 6):
        i+=1
        print(i)
        Display(i)


def main():
    Value = int(input("Enter a number : "))
    Display(Value)

if __name__ == "__main__":
    main()