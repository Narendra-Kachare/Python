# Accept input from user 

class Arithmetic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

    
    def Substration(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    

def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))

    obj1 = Arithmetic(Value1,Value2)

    Ret = obj1.Addition()
    print("Addtion is : ",Ret)

    Ret = obj1.Substration
    print("Substration is : ",Ret)

if __name__ == "__main__":
    main()