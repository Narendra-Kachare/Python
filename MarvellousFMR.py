# Module of FMR

# filterX(CheckEvenX,Arr)
def filterX(Task,Elements):
    Result = []
    for No in Elements:
        if Task(No) == True:
            Result.append(No)
    return Result


# mapX(IncrementX,R1)
def mapX(Task,Elements):
    Result = []
    for No in Elements:
        iRet = Task(No)
        Result.append(iRet)
    return Result

# reduceX(AddX,R2)
def reduceX(Task,Elements):
    Sum = 0
    for No in Elements:
        Sum = Task(Sum,No)
    return Sum
