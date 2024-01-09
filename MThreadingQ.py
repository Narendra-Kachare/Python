import threading
import queue
import os

def Addition(No1, No2, QArr):
    print(os.getpid())
    QArr.put(No1+No2)

def Substraction(No1, No2, QArr):
    print(os.getpid())
    QArr.put(No1-No2)

def Division(No1, No2, QArr):
    print(os.getpid())
    QArr.put(No1/No2)

def Multiplication(No1, No2, QArr):
    print(os.getpid())
    QArr.put(No1*No2)


def main():
    print("Demonstration of MultiThreading")

    No1 = int(input("Enter the first Number : "))
    No2 = int(input("Enter the second Number : "))

    # For return value create an object
    Q = queue.Queue()

    # Create Thread
    P1 = threading.Thread(args= (No1,No2,Q,), target = Addition,)
    P2 = threading.Thread(args= (No1,No2,Q,), target = Substraction)
    P3 = threading.Thread(args= (No1,No2,Q,), target = Division)
    P4 = threading.Thread(args= (No1,No2,Q,), target = Multiplication)

    # Start Thread
    P1.start()
    P2.start()
    P3.start()
    P4.start()

    # and Wait for each other join method
    P1.join()
    P2.join()
    P3.join()
    P4.join()

    while Q.empty() is  False:
        print(Q.get())

    

if __name__ == "__main__":
    main()