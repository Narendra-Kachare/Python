"""
Recursion in python
"""
i = 0


def Display():
    global i
    print("Inside Display",i)
    i+=1
    Display()


def main():
    try:
        Display()
    except RecursionError as robj:
        print("Error is : ",robj)

if __name__ == "__main__":
    main()