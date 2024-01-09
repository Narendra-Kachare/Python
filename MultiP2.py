# Demonstration of Multitasking - MProcessing and MThreading
import os
import multiprocessing

def Addition(No1,No2):
    print(os.getpid())
    return int(No1+No2)

def Substration(No1,No2):
    print(os.getpid())
    return int(No1-No2)

def Multiplication(No1,No2):
    print(os.getpid())
    return int(No1*No2)

def Division(No1,No2):
    print(os.getpid())
    return float(No1/No2)



def main():
    print("Demonstration of Multi Threading")
    
    No1 = int(input("Enter first number : \n"))
    No2 = int(input("Enter second number : \n"))


    P1 = multiprocessing.Process(args = (No1,No2,), target = Addition)
    P2 = multiprocessing.Process(args = (No1,No2,), target = Substration)
    P3 = multiprocessing.Process(args = (No1,No2,), target = Multiplication)
    P4 = multiprocessing.Process(args = (No1,No2,), target = Division)

    P1.start()
    P2.start()
    P3.start()
    P4.start()

    P1.join()
    P2.join()
    P3.join()
    P4.join()






if __name__ == "__main__":
    main()

    