# Demonstration of MTasking - MProcessing and MTasking
import multiprocessing
import os 


def Addition(No1,No2):
    print(No1+No2)

    

def Substration(No1,No2):
    print(os.getpid)
    print(No1-No2)

def Division(No1,No2):
    print(os.getpid)
    try:
        print(No1/No2)
    except ZeroDivisionError as zobj:
        print("Error is",zobj)



def Multiplication(No1,No2):
    print(os.getpid)
    print(No1*No2)


def main():
    print("Demonstration of MultiProcessing")
    print(os.getppid)

    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))
    


    # Create process
    P1 = multiprocessing.Process(target=Addition, args=(No1,No2,))
    P2 = multiprocessing.Process(target=Substration, args=(No1,No2,))
    P3 = multiprocessing.Process(target=Multiplication, args=(No1,No2,))
    P4 = multiprocessing.Process(target=Division, args=(No1,No2,))
    
    # Start Process
    P1.start()
    P2.start()
    P3.start()
    P4.start()

    # Join Process
    P1.join()
    P2.join()
    P3.join()
    P4.join()




if __name__ == "__main__":
    main()