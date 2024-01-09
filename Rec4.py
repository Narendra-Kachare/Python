"""
Recursion in python
"""


def Display():
    print("Inside Fun")
    Display()

def main():
    try:
        Display()
    except RecursionError as robj:
        print("Error is : ",robj)

if __name__ == "__main__":
    main()