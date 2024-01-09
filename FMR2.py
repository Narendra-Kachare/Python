"""
    Filter Map Reduce
"""
from functools import reduce

def CheckEven(No):
    if No % 2 == 0:
        return True
    else:
        return False
    
def Increment(No):
    return No+2

def Add(A,B):
    return A+B

def main():
    print("Demonstration of FMR")

    print("Enter the number of elements :")
    Length = int(input())

    Arr = list()
    print("Enter the elements : ")
    for Values in range(Length):
        try:
            Value = int(input())
            Arr.append(Value)
        except Exception as e:
            print("Error is %s" %e)
    print("Filter process initialisation")
    R1 = list(filter(CheckEven,Arr))
    print(R1)

    print("Map process initialisation")
    R2 = list(map(Increment,R1))
    print(R2)

    print("Reduce process initialisation")
    R3 = int(reduce(Add,R2))
    print(R3)





if __name__ == "__main__":
    main()