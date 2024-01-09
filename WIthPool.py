import multiprocessing
import os

def Square(No):
    
    return No*No


def main():
    print("Demonstration of WithPool Concept")

    Arr = list()
    Length = int(input("Enter the number of elements : "))
    print("Enter the elements : ")
    for i in range(Length):
        try:
            Value = int(input())
            Arr.append(Value)
        except ValueError as vobj:
            print("Error is : %s" %vobj)
        except Exception as eobj:
            print("Error is : ",eobj)


    iRet = list()

    P = multiprocessing.Pool()  
    iRet = P.map(Square,Arr)
    P.close()   # Light OFF
    P.join()    # Wait for them until they complete the task
    
    print(iRet)        

if __name__ == "__main__":
    main()