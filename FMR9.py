
CheckEvenx = lambda No : (No % 2 == 0)
IncrementX = lambda No : (No+2)
AddX = lambda A,B : A+B

# filterX(CheckEvenx,Arr)
def filterX(CheckEvenX,Arr):
    Result = list()
    for No in Arr:
        if CheckEvenX(No) == True:
            Result.append(No)
    return Result

# map(IncrementX,R1)
def mapX(IncrementX,R1):
    Result = list()
    for No in R1:
        Ret = IncrementX(No)
        Result.append(Ret)
    return Result

# reduce(AddX,R2)
def reduceX(Task, Elements):
    Sum =  0         # Sum - 0 gives local UnboundError
    for No in Elements:
        Sum = Task(Sum,No)
    return Sum

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