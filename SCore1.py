import time


def Fun(no):
    sum = 0
    for i in range(100):
        sum = sum + (no*no)
        print(sum)



def main():
    print("Demonstration of Map function in multiprocessing")

    StartTime = time.time()

    for i in range(100):
        iRet = Fun(i)
    
    EndTime = time.time()
    print("Time required to run application : ",EndTime-StartTime)

if __name__ == "__main__": 
    main()