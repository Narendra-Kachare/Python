# define multipleprocessing module and do multiprcessing in given task function
import os
import multiprocessing
from time import time

def Addition(ptr):
    Ans = 0
    for i in range(len(ptr)):
        Ans = Ans + ptr[i]
    print("Addition of all number : ",Ans)
    print("PID of given function is : ",os.getpid(),"\n")

def OddAdd(ptr):
    Ans = 0
    for i in range(len(ptr)):
        if((ptr[i] % 2) == 0):
            Ans = Ans + ptr[i]
    print("Addition of Odd number : ",Ans)
    print("PID of given function is : ",os.getpid(),"\n")

def EvenAdd(ptr):
    Ans = 0
    for i in range(len(ptr)):
        if((ptr[i] % 2) != 0):
            Ans = Ans + ptr[i]
    print("Addition of Even number is : ",Ans)
    print("PID of given function is : ",os.getpid(),"\n")


def main():
    Starttime = time()
    print("PID of running process will be : ",os.getpid())
    print("PPID of running parent process will be : ",os.getppid())
    Arr = [10,11,12,13,14,15,16,17,18,19,20]
    Addition(Arr)
    OddAdd(Arr)
    EvenAdd(Arr)
    Endtime = time()
    print(Endtime - Starttime)

if __name__ == "__main__":
    main()