"""
Recursion in python
"""
import sys

i = 1

def Display(no):
    global i

    if(i <= no):
        i+=1
        print("No")
        Display(no)
    
def main():
    
    Display(5)


if __name__ == "__main__":
    main()