# Demonstration of Multitasking - MProcessing and MThreading
import threading
import os

def Task1(Value):
    print(os.getpid())
    print("Executing the first task")
    for i in range(Value):
        print("Task1 ->",i)

def Task2(Value):
    print(os.getpid())
    print("Execution the second task")
    for i in range(Value):
        print("Task2 ->",i)

def main():
    print("Demonstration of Multi Processing")
    No1 = int(input("Enter the number : "))

    P1 = threading.Thread(target= Task1, args= (No1,))
    P2 = threading.Thread(target= Task2, args= (No1,))

    P1.start()
    P2.start()

    P1.join()
    P2.join()




if __name__ == "__main__":
    main()