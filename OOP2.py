# Accept input from user in class

class Arithmetic:
    def __init__(self):
        self.No1 = int(input("Enter first number : \n"))
        self.No2 = int(input("Enter second number : \n"))

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

    
    def Substration(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    

def main():


    obj1 = Arithmetic()

    Ret = obj1.Addition()
    print("Addtion is : ",Ret)

    Ret = obj1.Substration()
    print("Substration is : ",Ret)

if __name__ == "__main__":
    main()