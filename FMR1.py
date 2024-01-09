from functools import reduce

def CheckEven(No):
    if No % 2 == 0:
        return True
    else:
        return False
def Sub(a,b):
    return a-b

def Increase(No):
    return No+2

def Add(A,B):
    return A+B


def main():
    print("Demonstration of Filter Map Reduce")
    Data = [11,12,13,14,15,16,17,18,19,20]
    print(Data)

    Output = list(filter(CheckEven,Data))
    print(Output)

    MOutput = list(map(Increase,Output))
    print(MOutput)

    Result = reduce(Add,MOutput)
    print(Result)




if __name__ == "__main__":
    main()