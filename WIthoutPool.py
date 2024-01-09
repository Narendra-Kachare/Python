
def Square(No):
    return No*No


def main():
    print("Demonstration of WithPool Concept")

    Arr = [11,21,51,101]
    Result = []

    for Values in Arr:
        Ans = Square(Values)
        Result.append(Ans)
    
    print(Result)        

if __name__ == "__main__":
    main()