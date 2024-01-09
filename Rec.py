"""
    Recurssion is calling function from same function itself.
    factorial is the best example for recurssion
    
    # 7! = 7 * 6! = 7*6*5*4*3*2*1
    # 6! = 6 * 5! = 6*5*4*3*2*1
    # 5! = 5 * 4! = 5*4*3*2*1
    # 4! = 4 * 3! = 4*3*2*1
    # 3! = 3 * 2! = 3*2*1
    # 2! = 2 * 1  = 2*1
    # 1! or 0!    = 1 

"""

def Factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Factorial(n-1)
    
def Fibinocci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (Fibinocci(n-1)+ Fibinocci(n-2))

def main():
    iRet = 0
    Value = int(input("Enter the number : "))
    iRet = Factorial(Value)
    print("Factorial of ",Value," is ",iRet)

    iRet = Fibinocci(Value)
    print("Fibinocci number is : ",iRet)

if __name__ == "__main__":
    main()
