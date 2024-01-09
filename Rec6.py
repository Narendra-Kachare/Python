"""
Recursion in python
"""
import sys
def Display(no):
    if no == 0:
        return 0
    if no == 1:
        return print("*")
    else:
        return print("*") * Display(no-1)


def main():

    No = int(input("Enter no : "))
    Display(No)

if __name__ == "__main__":
    main()