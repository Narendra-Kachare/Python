"""
    Filter Map Reduce
"""
from functools import reduce

# def CheckEven(No):
#     if(No % 2 == 0):
#         return True
#     else:
#         return False

# def Incement(No):
#     return No+2

# def Add(No1,No2):
#     return No1+No2
CheckEvenX = lambda No : (No % 2 == 0)
IncrementX = lambda No : (No + 2)
AddX = lambda No1,No2 : (No1+ No2)



def main():
    print("Demonstration of Filter Map Reduce")

    print("Enter the number of elements : ")
    Length = int(input())

    Arr = list()
    print("Enter the elements : ")
    for Value in range(Length):
        try:
            Value = int(input())
        except ValueError as vobj:
            print("Error is : %s" %vobj)
        except Exception as E:
            print("Error is : ",E)
        Arr.append(Value)

    # print("Filter Process Initialisation")
    # R1 = list(filter(CheckEven,Arr))
    # print(R1)

    # print("Map Process Initialisation")
    # R2 = list(map(Increment,R1))
    # print(R2)


    # print("Reduce Process Initialisation")
    # R3 = functools.reduce(Add: (No1 + No2),R2)
    # print(R3)
    print("Reduce result is : ")
    print(reduce(AddX,map(IncrementX,filter(CheckEvenX,Arr))))

if __name__ == "__main__":
    main()