"""
    Filter Map Reduce
"""
import functools


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

    print("Filter Process Initialisation")
    R1 = list(filter(lambda No : (No % 2 == 0),Arr))
    print(R1)

    print("Map Process Initialisation")
    R2 = list(map(lambda No : (No+2),R1))
    print(R2)


    print("Reduce Process Initialisation")
    R3 = functools.reduce(lambda No1,No2 : (No1 + No2),R2)
    print(R3)

if __name__ == "__main__":
    main()