
from MarvellousFMR import *

CheckEvenx = lambda No : (No % 2 == 0)
IncrementX = lambda No : (No+2)
AddX = lambda A,B : A+B


def main():
    print("Demonstration od Filter Map Reduce")
    print("Enter number of elements : ")
    Length = int(input())

    Arr = list()
    for Values in range(Length):
        Values = int(input())
        Arr.append(Values)

    R1 = list(filterX(CheckEvenx,Arr))
    print(R1)

    R2 = list(mapX(IncrementX,R1))
    print(R2)

    R3 = reduceX(AddX,R2)
    print(R3)

if __name__ == "__main__":
    main()