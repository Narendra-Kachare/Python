"""
    Filter Map Reduce
"""
from functools import reduce





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



    print("Reduce result is : ")
    # CheckEvenX = lambda No : (No % 2 == 0)
    # IncrementX = lambda No : (No + 2)
    # AddX = lambda No1,No2 : (No1+ No2)
    
    #print(reduce(AddX,map(IncrementX,filter(CheckEvenX,Arr))))

    print(reduce(lambda No1,No2 : (No1+No2),map(lambda No : (No+2),filter(lambda No : (No%2 == 0),Arr))))

if __name__ == "__main__":
    main() 
